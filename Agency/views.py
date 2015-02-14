from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from Agency.models import Contest1


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request,'about.html', {})

def friend(request):
    return render(request, 'friend.html', {})

def contest1(request):
    return render(request,'contest1.html', {'contest1': Contest1.objects.all()})

def contest2(request):
	return render(request, 'contest2.html', {})
	
def contest3(request):
	return render(request, 'contest3.html', {})
