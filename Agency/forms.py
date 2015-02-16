from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from Agency.models import Contest1
from Agency.models import Contest2

class Contest1Form(forms.Form):

    class Meta:
	    model = Contest1
	    fields = ['email', 'name', 'age']
		
    email = forms.EmailField(label="Your email", required=True)
    name = forms.CharField(max_length=128)
    age = forms.IntegerField()
	
class Contest2Form(forms.Form):
	class Meta:
		model = Contest2
		fields = ['first_name','last_name','age','email','zip','phone']
	first_name = forms.CharField(max_length=128)
	last_name = forms.CharField(max_length=128)
	age = forms.IntegerField()
	email = forms.EmailField(label = "Your Email", required = True)
	zip = forms.IntegerField()
	phone = forms.IntegerField()

	