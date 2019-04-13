from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

debug = True

def welcome(request):
    # This is the first html page
    return render(request, 'Scheduler/welcome.html')

def calendar(request):
    # This is the first html page    
    }
    return render(request, 'Scheduler/calendar.html')

def file(request):
    # This is the first html page
    return render(request, 'Scheduler/file.html')
