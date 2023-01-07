from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
        {"num_meetings": Meeting.objects.count()})

def about(request):
    aboutMe = "Learning Django via PluralSight"
    return HttpResponse(aboutMe)