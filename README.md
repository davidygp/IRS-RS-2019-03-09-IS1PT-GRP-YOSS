# SECTION 1 : PROJECT TITLE
### Yoga Class Scheduling System
<img width="812" alt="welcome" src="https://user-images.githubusercontent.com/48171290/54080819-80836a80-4333-11e9-9f1d-7f21123d454f.png">

# SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
With the overwhelming welcome for the yoga activity, A * yoga has opened its 5th new yoga studio in Singapore recently. It targets to provide 100+ different styles of yoga classes every week with experienced yoga masters and well decorated yoga rooms to customers. However, with the various yoga classes, complicated yoga master skills and available dates, it is very troublesome to plan a weekly yoga class schedule.

Our group, containing 5 part-time students under reasoning system course, decided to take this chance to help A * yoga studio by applying knowledge we have learnt from the course. Hence, our group developed an automated scheduling system, Yoga Class Scheduling System (YOSS), to generate a weekly yoga class schedule based on the default system data or data provided by user.

Inside YOSS, we first set out to perform knowledge acquisition by interviewing a subject matter expert. To build the system, we decided to utilize Search and Rule-Based Reasoning as tools through Django web framework and KIE server to perform the scheduling task. What’s more, we have come out with a calendar user interface to display the scheduling results to users.

Our team learned a lot in the process of working on this project. We got the chance to apply techniques, such as search algorithm and rule-based reasoning, which we learned in our lectures and workshops in this viable business application scenario, and also picked up technical skills which would surely prove useful in the future course of our work.


# SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name | Student ID (MTech Applicable)| Work Items (Who Did What) | Email (Optional) |
| :---: | :---: | :---: | :---: |
| LI DUO  | A0195364W | Business idea generation, UI Design | e0384995@u.nus.edu |
| LIM CHONG SENG HERMANN | A0195392U | Business idea generation, Django web framework, Overall integration | e0385023@u.nus.edu |
| LU JIAHAO | A0091835Y | Business idea generation, KIE server design, OptaPlanner rules, project video | e0384293@u.nus.edu |
| YAM GUI PENG DAVID | A0195315A | Business idea generation, KIE server design, OptaPlanner rules, Overall integration | e0384946@u.nus.edu |
| ZHAO YAZHI | A0195305E | Business idea generation, domain expert interview, data gathering and preparation, project report | e0384936@u.nus.edu |

# SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
[![Watch the video](https://user-images.githubusercontent.com/48171290/54084381-cad40e00-436a-11e9-8c73-83abc096a3f2.PNG)](https://www.youtube.com/watch?v=vu1eQ-0R4e8&feature=youtu.be)


# SECTION 5 : USER GUIDE
[ 1 ] Setup the Virtual Environment Setup the KIE Server environment. Install additional necessary libraries. Note: This application works in python 3 only.

### Installing Virtual Box:
1. Download and install Virtualbox software: https://www.virtualbox.org/wiki/Downloads
2. Download and iss-vm virtual machine (an Appliance) from:

http://bit.ly/iss-vm-v18a ( part 1 about 13 GB in file size )

http://bit.ly/iss-vm-v18b ( part 2 about 13 GB in file size )

3. Start Virtualbox software
4. Click File -> Import Appliance
5. Click Start to use iss-vm


### Import the files:

$ git clone https://github.com/davidygp/IRS-RS-2019-03-09-IS1PT-GRP-YOSS

### Setup of KIE Server:
1. Start KIE Server
2. Unzip the file ./IRS-RS-2019-03-09-IS1PT-GRP-YOS/SystemCode/YogaClassScheduler1-2
3. Import the Project YogaClassScheduler-3
4. Deploy the Project YogaClassScheduler-3

### Setup of Python Environment:

$ pip install pandas

$ pip install django

$ pip install requests

### Start Python django server:

$ cd ./IRS-RS-2019-03-09-IS1PT-GRP-YOS/SystemCode

$ python manage.py runserver

Go to URL using web browser http://127.0.0.1:8000/


# SECTION 6 : PROJECT REPORT / PAPER
<Github File Link>  https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard/tree/master/ProjectReport/Report.pdf

# SECTION 7 : MISCELLANEOUS
Scheduling Data.xlsx
+ Full Scheduling Dataset

Scheduling Data (simple case 1) .xlsx
Scheduling Data (simple case 2) .xlsx
Scheduling Data (simple case 3) .xlsx
+ Sample Scheduling Dataset

Scheduling Data (Wrong Format) .xlsx
+ Sample Scheduling Data with the wrong format (Note: will not work)
