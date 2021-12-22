from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.conf import settings


# Create your views here.

def index(request):
    if request.method == "GET":
        pro = product.objects.all()
        img = backimage.objects.all()
    context = {"Tittle": "index", "pro": pro, "img": img}
    return render(request, "index.html", context)
