from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from Agency.models import Contest1

class Contest1Form(forms.Form):

    class Meta:
	    model = Contest1
	    fields = ['email', 'name', 'age']
		
    email = forms.EmailField(label="Your email", required=True)
    name = forms.CharField(max_length=128)
    age = forms.IntegerField()

	