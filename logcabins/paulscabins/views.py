# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
#from .forms import signInForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
import re
from .models import Testimonial, PhotoUpload

# Create your views here.

def index(request):
    return render(request, 'paulscabins/home.html')

def aboutus(request):
    return render(request, 'paulscabins/aboutus.html')

def yourloghome(request):
    return render(request, 'paulscabins/yourloghome.html')

def logrestoration(request):
    return render(request, 'paulscabins/logrestoration.html')

def gallery(request):
    p = PhotoUpload.objects.all()
    return render(request, 'paulscabins/gallery.html', {'photos': p})

def testimonials(request):
    p = Testimonial.objects.all()
    return render(request, 'paulscabins/testimonials.html', {'testimonials': p})