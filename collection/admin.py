# -*- coding: utf-8 -*-
from django.contrib import admin

from django.http import HttpResponse
from django.shortcuts import render_to_response
from collection.models import collection
from django.shortcuts import render
# Register your models here.
def reflush(request):
    request.encoding = 'utf-8'
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin.html', context)
    