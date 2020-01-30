from re import search

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def search(request, no_attend):
    return HttpResponse(f'no of attanded student {no_attend}')

def showstudent(request):
    return HttpResponse('Show dashboard')