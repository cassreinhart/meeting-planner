from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting

def welcome(request):
    return render(request, 'website/welcome.html', #relative path to the templates dir
                {"meetings": Meeting.objects.all()}) #retrieve num of meetings currently in db

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("My name is Cassandra and I am a web developer.")