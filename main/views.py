from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(req):
    return HttpResponse("<h1>Hello World</h1>")
