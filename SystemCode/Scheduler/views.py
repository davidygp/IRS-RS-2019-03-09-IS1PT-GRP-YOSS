from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import TemplateView
import pandas as pd
import html

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
    
    print(file_location)

    df = pd.read_excel(file_location)
    
#    print(df.columns)
#    print(df['MasterName'][0])

    context = {
    'events': [
    {
    'id': '3',
    'resourceId': 'c',
    'title': 'Class C',
    'start': '2019-04-18 11:00',
    'end': '2019-04-18 12:00'
    },
    {
    'id': '4',
    'resourceId': 'd',
    'title': 'Class D',
    'start': '2019-04-18 16:00',
    'end': '2019-04-18 17:00'
    }
    ]
    }

    return render(request, 'Scheduler/calendar.html', {'temp':context})

def file(request):
    # This is the first html page
    
    return render(request, 'Scheduler/file.html')

def file1(request):
    # This is the first html page

    return render(request, 'Scheduler/file.html')
