from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from Agency.models import Contest1, Contest2, Friend, Contest3
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from Agency.forms import Contest1Form, Contest2Form, Friend3Form, Contest3Form


def home(request):
    return render(request, 'home.html', {})


def splash(request):
    return render(request, 'splash.html', {})


def thanks(request):
    return render(request, 'thanks.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def friend(request):
    if request.method == 'POST':
        form3 = Friend3Form(request.POST)
        if form3.is_valid():
            f = Friend()
            f.user_frist_name = form3.cleaned_data["user_frist_name"]
            f.age = form3.cleaned_data["age"]
            f.user_email = form3.cleaned_data["user_email"]
            f.friend_name1 = form3.cleaned_data["friend_name1"]
            f.friend1_email = form3.cleaned_data["friend1_email"]
            f.friend_name2 = form3.cleaned_data["friend_name2"]
            f.friend2_email = form3.cleaned_data["friend2_email"]
            f.friend_name3 = form3.cleaned_data["friend_name3"]
            f.friend3_email = form3.cleaned_data["friend3_email"]
            f.save()
            return HttpResponseRedirect("/thanks")
    elif request.method == 'GET':
        form3 = Friend3Form()
    else:
        return HttpResponseRedirect("/404/")
    return render(request, 'friend.html', {"form3": form3})


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
    return render(request, "contest2.html", {"form2": form2})


def contest3(request):
    if request.method == 'POST':
        form3 = Contest3Form(request.POST)
        if form3.is_valid():
            z = Contest3()
            z.first_name = form3.cleaned_data["first_name"]
            z.last_name = form3.cleaned_data["last_name"]
            z.age = form3.cleaned_data["age"]
            z.email = form3.cleaned_data["email"]
            z.zip = form3.cleaned_data["zip"]
            z.phone = form3.cleaned_data["phone"]
            z.save()
            return HttpResponseRedirect("/friend")
    elif request.method == 'GET':
        form3 = Contest3Form()
    else:
        return HttpResponseRedirect("/404/")
    return render(request, "contest3.html", {"form3": form3})


def contest1(request):
    if request.method == 'POST':
        form = Contest1Form(request.POST)
        if form.is_valid():
            c = Contest1()
            c.email = form.cleaned_data["email"]
            c.age = form.cleaned_data["age"]
            c.name = form.cleaned_data["name"]
            c.zip = form2.cleaned_data["zip"]
            c.save()
            return HttpResponseRedirect("/friend")
    elif request.method == 'GET':
        form = Contest1Form()
    else:
        return HttpResponseRedirect("/404/")

    return render(request, "contest1.html", {"form": form})
