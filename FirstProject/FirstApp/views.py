from django.shortcuts import render
from FirstApp import views
from django.http import HttpResponce

# Create your views here.
def disply(request):
    ss=<h1> Welcome to Django Session </h1>
    return HttpResponce(ss);