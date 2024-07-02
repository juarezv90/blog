from rest_framework import views
from django.shortcuts import render
from . import models
from . import serializers
# Create your views here.

def Index(request):
    return render(request, "home.html", {})