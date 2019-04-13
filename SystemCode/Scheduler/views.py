from django.shortcuts import render

# Create your views here.

debug = True

def welcome(request):
    # This is the first html page
    return render(request, 'Recommender/welcome.html')

def calendar(request):
    # This is the first html page
    return render(request, 'Recommender/calendar.html')

def file(request):
    # This is the first html page
    return render(request, 'Recommender/file.html')