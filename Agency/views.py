from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from Agency.models import Contest1
from Agency.models import Contest2
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from Agency.forms import Contest1Form
from Agency.forms import Contest2Form


def home(request):
    return render(request, 'home.html', {})
	
def thanks(request):
    return render(request, 'thanks.html', {})

def about(request):
    return render(request,'about.html', {})

def friend(request):
    return render(request, 'friend.html', {})

#def contest1(request):
#    return render(request,'contest1.html', {'contest1': Contest1.objects.all()})

def contest2(request):
	if request.method == 'POST':
	    form2 = Contest2Form(request.POST)
	    if form2.is_valid():
			x = Contest2()
			x.first_name = form2.cleaned_data["first_name"]
			x.last_name = form2.cleaned_data["last_name"]
			x.age = form2.cleaned_data["age"]
			x.email = form2.cleaned_data["email"]
			x.zip = form2.cleaned_data["zip"]
			x.phone = form2.cleaned_data["phone"]
			x.save()
			return HttpResponseRedirect("/friend")
	elif request.method == 'GET':
		form2 = Contest2Form()
	else:
		return HttpResponseRedirect("/404/")
	return render(request, "contest2.html", {"form2" : form2})
	
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
		    return HttpResponseRedirect("/thanks")
    elif request.method == 'GET':
	    form = Contest1Form()
    else:
	    return HttpResponseRedirect("/404/")
		
    return render(request, "contest1.html", {"form" : form})
