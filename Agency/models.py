from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models

class Contest1(models.Model):
    email = forms.EmailField(label="Your Email")
    name = forms.CharField(max_length=128)
    age = forms.IntegerField()
	
	