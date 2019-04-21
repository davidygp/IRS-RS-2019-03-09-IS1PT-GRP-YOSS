from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import TemplateView
import pandas as pd
import html
import requests

# Create your views here.

debug = True

def welcome(request):
    # This is the first html page    
    return render(request, 'Scheduler/welcome.html')

def calendar(request):
    # This is the first html page    

    if request.method == 'POST' and request.FILES['document']:
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

    file_location = ''.join([fs.location, '/', uploaded_file.name])
    
#    print(file_location)

    context = {

    'resources': [
                { 'id': 'a', 'title': 'Room Yama' },
                { 'id': 'b', 'title': 'Room Asana', 'eventColor': 'green' },
                { 'id': 'c', 'title': 'Room Niyama', 'eventColor': 'orange' },
                { 'id': 'd', 'title': 'Room Drishti', 'eventColor': 'red' },
            ],

    'events': [
    {
    'id': '3',
    'resourceId': 'c',
    'title': 'Class C',
    'start': '2019-04-21 11:00',
    'end': '2019-04-21 12:00'
    },
    {
    'id': '4',
    'resourceId': 'd',
    'title': 'Class D',
    'start': '2019-04-21 16:00',
    'end': '2019-04-21 17:00'
    }
    ]
    }

    xml = writePostXML(file_location)

    if request.session["optaplanner_started"] == False:
        PUTResponse = doPUTRequest()
        if str(PUTResponse.status_code)[0] == "2":
            print('PUT: response:2**')
            request.session["optaplanner_started"] = True
            POSTResponse = doPOSTRequest(xml)
            print('poststatuecode1:', POSTResponse.status_code)
            print('poststatuecode2:', POSTResponse.text)
        else:
            print('PUT: response:not2**')
            print(PUTResponse.status_code)
            print(PUTResponse.text)
            print('Restarting, DEL, PUT, POST')
            doDELRequest()
            doPUTRequest()
            request.session["optaplanner_started"] = True
            POSTResponse = doPOSTRequest(xml)
            print('New status code is', PUTResponse.status_code)
    
    if str(POSTResponse.status_code)[0] == "2":
        print('doGet')
        GETResponse = doGETRequest()
        print('getstatuecode1:', GETResponse.status_code)
        print('getstatuecode2:', GETResponse.text)

    return render(request, 'Scheduler/calendar.html', {'temp':context})

def file(request):
    # This is the first html page
    request.session["optaplanner_started"] = False
    doDELRequest()
    return render(request, 'Scheduler/file.html')

def createClassAssignmentObject(df):
    xml = ['  <classassignmentList>']
    for index, row in df.iterrows():
        xml.append('    <com.iss_rs.yogaclassscheduler.ClassAssignment>')
        xml.append('      <id>{0}</id>'.format(index))
        xml.append('      <timeslot>')
        xml.append('        <id>{0}</id>'.format(index))
        xml.append('        <day>{0}</day>'.format(row['day']))
        xml.append('        <shift>{0}</shift>'.format(row['shift']))
        startTimeInMins = convertToMins(str(row['startingTime']))
        xml.append('        <startingTime>{0}</startingTime>'.format(startTimeInMins))
        endingTimeInMins = convertToMins(str(row['endingTime']))
        xml.append('        <endingTime>{0}</endingTime>'.format(endingTimeInMins))
        xml.append('        <availableDurationMins>{0}</availableDurationMins>'.format(row['availableDurationMins']))
        xml.append('      </timeslot>')        
        xml.append('    </com.iss_rs.yogaclassscheduler.ClassAssignment>')
    xml.append('  </classassignmentList>')
#        print('\n'.join(xml))

    return xml

def createYogaClassObject(df):
    xml = ['  <yogaclassList>']
    for index, row in df.iterrows():
        xml.append('    <com.iss_rs.yogaclassscheduler.YogaClass>')
        xml.append('      <id>{0}</id>'.format(index))
        xml.append('      <className>{0}</className>'.format(row['className']))
        xml.append('      <classCategory>{0}</classCategory>'.format(row['classCategory']))
        xml.append('      <classDurationMins>{0}</classDurationMins>'.format(row['classDurationMins']))
        xml.append('    </com.iss_rs.yogaclassscheduler.YogaClass>')
    xml.append('  </yogaclassList>')
#        print('\n'.join(xml))

    return xml

def createYogaMasterObject(df):
    xml = ['  <masterList>']
    for index, row in df.iterrows():
        xml.append('    <com.iss_rs.yogaclassscheduler.Master>')
        xml.append('      <id>{0}</id>'.format(index))
        xml.append('      <masterName>{0}</masterName>'.format(row['masterName']))
        yogaClassList = getYogaClassList(row['availableCourseNames'])
        xml += yogaClassList
        dayList = getDayList(row['availableDays'])
        xml += dayList
        xml.append('    </com.iss_rs.yogaclassscheduler.Master>')
    xml.append('  </masterList>')
#        print('\n'.join(xml))

    return xml

def createYogaRoomObject(df):
    xml = ['  <roomList>']
    for index, row in df.iterrows():
        xml.append('    <com.iss_rs.yogaclassscheduler.Room>')
        xml.append('      <id>{0}</id>'.format(index))
        xml.append('      <roomName>{0}</roomName>'.format(row['roomName']))
        xml.append('    </com.iss_rs.yogaclassscheduler.Room>')
    xml.append('  </roomList>')
#        print('\n'.join(xml))

    return xml

def getYogaClassList(availableCourses):
    yogaClassList = ['      <availableYogaClassList>']
    newList =  availableCourses.split(", ")
    for course in newList:
        yogaClassList.append('        <string>{0}</string>'.format(course))
    yogaClassList.append('      </availableYogaClassList>')
#    print('\n'.join(yogaClassList))

    return yogaClassList

def getDayList(availableDays):
    dayList = ['      <availableDayList>']
    newList =  availableDays.split(", ")
    for day in newList:
        dayList.append('        <string>{0}</string>'.format(day))
    dayList.append('      </availableDayList>')
#    print('\n'.join(dayList))

    return dayList

def convertToMins(time):
    timeSplit = time.split(":")
    newTime = (int(timeSplit[0]) * 60) + int(timeSplit[1])
#    print(newTime)

    return newTime

def writePostXML(file_location):

    df = pd.read_excel(file_location)

    pop_Yoga_Timeslots = pd.read_excel(file_location, sheetname="Yoga Timeslots")
    pop_Yoga_Class = pd.read_excel(file_location, sheetname="Yoga Class")
    pop_Yoga_Masters = pd.read_excel(file_location, sheetname="Yoga Masters")
    pop_Yoga_Rooms = pd.read_excel(file_location, sheetname="Yoga Rooms")

    xml_Yoga_Timeslots = createClassAssignmentObject(pop_Yoga_Timeslots)
    xml_Yoga_Class = createYogaClassObject(pop_Yoga_Class)
    xml_Yoga_Masters = createYogaMasterObject(pop_Yoga_Masters)
    xml_Yoga_Rooms = createYogaRoomObject(pop_Yoga_Rooms)

    xml_problem =['<planning-problem class="com.iss_rs.yogaclassscheduler.ClassSchedule">']
    xml_problem.append('  <id>0</id>')
    xml_problem += xml_Yoga_Timeslots
    xml_problem += xml_Yoga_Class
    xml_problem += xml_Yoga_Masters
    xml_problem += xml_Yoga_Rooms
    xml_problem.append('</planning-problem>')

    f = open('testxml.xml','w')
    f.write('\n'.join(xml_problem))
    f.close()

#    print('\n'.join(xml_slotList));

    return xml_problem

def doPUTRequest():
    url = "http://localhost:8080/kie-server/services/rest/server/containers/YogaClassScheduler_1.0.0/solvers/YogaClassSchedulerSolver"

    payload = "<solver-instance>\n  <solver-config-file>com/iss_rs/yogaclassscheduler/YogaClassSchedulerConfig.solver.xml</solver-config-file>\n</solver-instance>"
    headers = {
        'X-KIE-ContentType': "xstream",
        'Content-Type': "application/xml",
        'Authorization': "Basic d2JhZG1pbjp3YmFkbWlu",
        'cache-control': "no-cache",
        'Postman-Token': "679c1460-ab0c-486c-a0c1-50f63a908b30"
        }

    response = requests.request("PUT", url, data=payload, headers=headers)
    return response

def doPOSTRequest(xml_problem):
    url = "http://localhost:8080/kie-server/services/rest/server/containers/YogaClassScheduler_1.0.0/solvers/YogaClassSchedulerSolver/state/solving"

    payload = '\n'.join(xml_problem)
    headers = {
        'X-KIE-ContentType': "xstream",
        'Content-Type': "application/xml",
        'Authorization': "Basic d2JhZG1pbjp3YmFkbWlu",
        'cache-control': "no-cache",
        'Postman-Token': "b1df6a63-ceb7-43b1-aa91-e53838e9832a"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

def doGETRequest():
    url = "http://localhost:8080/kie-server/services/rest/server/containers/YogaClassScheduler_1.0.0/solvers/YogaClassSchedulerSolver/bestsolution"

    payload = ""
    headers = {
        'Authorization': "Basic d2JhZG1pbjp3YmFkbWlu",
        'cache-control': "no-cache",
        'Postman-Token': "d8e16bd8-9b95-4f95-b425-f0afcaffaebc"
        }

    response = requests.request("GET", url, data=payload, headers=headers)
    return response


def doDELRequest():
    url = "http://localhost:8080/kie-server/services/rest/server/containers/YogaClassScheduler_1.0.0/solvers/YogaClassSchedulerSolver"

    payload = ""
    headers = {
        'Authorization': "Basic d2JhZG1pbjp3YmFkbWlu",
        'cache-control': "no-cache",
        'Postman-Token': "2394e08b-ff45-4884-acb8-e14163539a19"
        }

    response = requests.request("DELETE", url, data=payload, headers=headers)
    return response






