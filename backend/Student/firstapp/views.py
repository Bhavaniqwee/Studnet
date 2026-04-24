from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def info(request):
    return HttpResponse('I am going to get job this year')