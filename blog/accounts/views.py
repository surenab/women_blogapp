from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return HttpResponse("Home page")



def home2(request):
    return HttpResponse(f"Home page after logaut: No user info")