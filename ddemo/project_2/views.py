from http.client import HTTPResponse
from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.



def module3(request):
    date = datetime.datetime.now()
    return HttpResponse("<h1>Current Date and Time is {}</h1>".format(date.strftime("%X")))