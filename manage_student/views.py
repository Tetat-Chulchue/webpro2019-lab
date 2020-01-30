from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('List of Student')

def add_student(request):
    return HttpResponse('Add Student')

def edit_student(request, id):
    return HttpResponse('Edit Student {}'.format(id))

def subject(request):
    return HttpResponse('List of Subject')

def add_subject(request):
    return HttpResponse('Add Subject')

def edit_subject(request, id):
    return HttpResponse('Edit Subject {}'.format(id))
    
