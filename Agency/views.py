from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request,'about.html', {})

def friend(request):
    return render(request, 'friend.html', {})

def contest1(request):
    return render(request,'contest1.html', {})

def contest2(request):
	return render(request, 'contest2.html', {})
	
def contest3(request):
	return render(request, 'contest3.html', {})
