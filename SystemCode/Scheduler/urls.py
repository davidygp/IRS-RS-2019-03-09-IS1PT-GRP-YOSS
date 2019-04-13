from django.urls import path

from . import views

app_name = 'Scheduler'
urlpatterns = [
    path('', views.welcome, name='welcome'),
#    path('eligibility/', views.eligibility, name='eligibility'),
    path('calendar/', views.calendar, name='calendar'),
    path('file/', views.file, name='file'),

    #path('spending/', views.spending, name='spending'),
    #path('bank/', views.bank, name='bank'),
    #path('end/', views.end, name='end')
]
