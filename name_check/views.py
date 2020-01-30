from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def inclass(request):
    return HttpResponse('Hello World! Teacher')

def course(request, course_id):
    return HttpResponse('This Course is {}'.format(course_id))

def qrcode(request):
    return HttpResponse('Picture QR Code')