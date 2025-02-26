from django.shortcuts import render
from django.http import HttpResponse

def aboutme(request):
    return HttpResponse("This is the about page")
