# SECTION 1 : PROJECT TITLE
### Yoga Class Scheduling System
<img width="812" alt="welcome" src="https://user-images.githubusercontent.com/48171290/54080819-80836a80-4333-11e9-9f1d-7f21123d454f.png">

# SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
With the overwhelming welcome for the yoga activity, A * yoga has opened its 5th new yoga studio in Singapore recently. It targets to provide 100+ different styles of yoga courses every week with experienced yoga masters and well decorated yoga rooms to customers. However, with the various yoga courses, complicated yoga master skills and available dates, it is very troublesome to plan a weekly yoga class schedule.

Our group, containing 5 part-time students under reasoning system course, decided to take this chance to help A * yoga studio by applying knowledge we have learnt from the course. Hence, our group developed an automated scheduling system, Yoga Class Scheduling System, to generate a weekly yoga class schedule based on the default system data or data provided by user.

Inside the Yoga Class Scheduling System, we first set out to perform knowledge acquisition by interviewing a subject matter expert. To build the system, we decided to utilize Search and Rule-Based Reasoning as tools through Django web framework and KIE server to perform the scheduling task. What’s more, we have come out with a calendar user interface to display the scheduling results to users.

Our team learned a lot in the process of working on this project. We got the chance to apply techniques, such as search algorithm and rule-based reasoning, which we learned in our lectures and workshops in this viable business application scenario, and also picked up technical skills which would surely prove useful in the future course of our work.

# SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name | Student ID (MTech Applicable)| Work Items (Who Did What) | Email (Optional) |
| :---: | :---: | :---: | :---: |
| LI DUO  | A0195364W | Business idea generation, UI Design | e0384995@u.nus.edu |
| LIM CHONG SENG HERMANN | A0195392U | Business idea generation, Django web framework | e0385023@u.nus.edu |
| LU JIAHAO | A0091835Y | Business idea generation, KIE server design, OptaPlanner rules, project video | e0384293@u.nus.edu |
| YAM GUI PENG DAVID | A0195315A | Business idea generation, KIE server design, OptaPlanner rules | e0384946@u.nus.edu |
| ZHAO YAZHI | A0195305E | Business idea generation, domain expert interview, data gathering and preparation, project report | e0384936@u.nus.edu |

# SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
[![Watch the video](https://user-images.githubusercontent.com/48171290/54084381-cad40e00-436a-11e9-8c73-83abc096a3f2.PNG)](https://www.youtube.com/watch?v=vu1eQ-0R4e8&feature=youtu.be)


# SECTION 5 : USER GUIDE
[ 1 ] To run the system in any machine with anaconda 3 installed

$ git clone https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard

$ cd ./IRS-MR-2019-01-19-IS1PT-GRP-MRCard/SystemCode

$ source activate ./venv/MRCard-env

(MRCard-env) $ python manage.py runserver

Go to URL using web browser http://127.0.0.1:8000/

$ (MRCard-env) $ source deactivate

[ 2 ] To run the system in other/local machine: Install additional necessary libraries. This application works in python 3 only.

$ pip install anaconda 3 

$ git clone https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard

$ cd ./IRS-MR-2019-01-19-IS1PT-GRP-MRCard/SystemCode

$ source activate ./venv/MRCard-env

(MRCard-env) $ python manage.py runserver

Go to URL using web browser http://127.0.0.1:8000/

$ (MRCard-env) $ source deactivate

# SECTION 6 : PROJECT REPORT / PAPER
<Github File Link>  https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard/tree/master/ProjectReport/Report.pdf

# SECTION 7 : MISCELLANEOUS
MRCard Survey Result.xlsx
+ Results of survey
+ Insights derived, which helped on features selection that are subsequently used in our system

Interview with Hu Juan.mps
+ Audio of the interview process with domain expert

Card Data - Bank Card Data (Cleaned_v2).csv
+ Data that used in the backend 

Data Fields - Sheet1.csv
+ Variables that used in the backend and rules
