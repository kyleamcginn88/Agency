from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from Agency.models import Contest1
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from Agency.forms import Contest1Form


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request,'about.html', {})

def friend(request):
    return render(request, 'friend.html', {})

#def contest1(request):
#    return render(request,'contest1.html', {'contest1': Contest1.objects.all()})

def contest2(request):
	return render(request, 'contest2.html', {})
	
def contest3(request):
	return render(request, 'contest3.html', {})
	

	
def contest1(request):
    if request.method == 'POST':
	    form = Contest1Form(request.POST)
	    if form.is_valid():
		    c = Contest1()
		    c.email = form.cleaned_data["email"]
		    c.age = form.cleaned_data["age"]
		    c.name = form.cleaned_data["name"]
		    c.save()
		    return HttpResponseRedirect("/thanks/")
    elif request.method == 'GET':
	    form = Contest1Form()
    else:
	    return HttpResponseRedirect("/404/")
		
    return render(request, "contest1.html", {"form" : form})
