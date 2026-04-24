from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addition(request):
    return HttpResponse("Addition of two numbers id : 4")