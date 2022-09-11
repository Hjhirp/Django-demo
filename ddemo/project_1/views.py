from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello World</h1>")

def secondformat(request):
	return HttpResponse("<h1><I>Hello World</I></h1>")