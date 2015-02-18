from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from Agency.models import Contest1, Contest2, Contest3, Friend


class Contest1Form(forms.Form):
    class Meta:
        model = Contest1
        fields = ['email', 'first_name','last_name', 'age', 'zip']

    email = forms.EmailField(label="Your email", required=True)
    first_name = forms.CharField(max_length=128, required=True)
    zip = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)

	
class Contest2Form(forms.Form):
    class Meta:
        model = Contest2
        fields = ['first_name', 'last_name', 'age', 'email', 'zip', 'phone']
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(label="Your Email", required=True)
    zip = forms.IntegerField(required=True)
    phone = forms.IntegerField(required=True)
	
	
class Contest3Form(forms.Form):
    class Meta:
        model = Contest3
        fields = ['first_name', 'last_name', 'age', 'email', 'zip', 'phone']
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(label="Your Email", required=True)
    zip = forms.IntegerField(required=True)
    phone = forms.IntegerField(required=True)

	
class Friend3Form(forms.Form):
    class Meta:
        model = Friend
        fields = ['user_frist_name', 'age', 'user_email', 'friend_name1',
                  'friend1_email', 'friend_name2', 'friend2_email',
                  'friend_name3', 'friend3_email']
    user_frist_name = forms.CharField(max_length=128)
    age = forms.IntegerField()
    user_email = forms.EmailField(label="Your Email", required=True)
    friend_name1 = forms.CharField(max_length=128)
    friend1_email = forms.EmailField(label="Friend 1", required=True)
    friend_name2 = forms.CharField(max_length=128)
    friend2_email = forms.EmailField(label="Friend 2", required=True)
    friend_name3 = forms.CharField(max_length=128)
    friend3_email = forms.EmailField(label="Friend 3", required=True)
