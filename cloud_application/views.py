# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def airpollution(request):
    items=AirPollution.objects.all()
    context={
    'items' : items,
    'header' : 'AirPollution'
    }
    return render(request, 'index.html', context)
    