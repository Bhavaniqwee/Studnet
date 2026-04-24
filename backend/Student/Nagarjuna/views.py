from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def added(request):
    return HttpResponse('View from Nagarjuna!!')