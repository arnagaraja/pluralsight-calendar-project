from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")

def about(request):
    aboutMe = "Learning Django via PluralSight"
    return HttpResponse(aboutMe)