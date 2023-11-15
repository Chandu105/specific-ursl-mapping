from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ravindra(request):
    return HttpResponse('<h1>new zealand world cup hero rachin ravindra</h1>')
def williamson(request):
    return HttpResponse('<h1> He is a true legend of the game</h1>')