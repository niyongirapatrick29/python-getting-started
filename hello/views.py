from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    #greeting = Greeting()
    #greeting.save()

    #greetings = Greeting.objects.all()

    return render(request, "db.html")

def home(request):
    movies = Movie.objects.all()  
    return render(request,'home.html',{'movies' :movies})

def movieDetail(request, movieId):
    movieDetails = Movie.objects.get(movieId=movieId)
    return render(request,'movieDetails.html',{'movieDetails' :movieDetails})