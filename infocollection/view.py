# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

#首页选择前台还是后台
def index(request):
     return render(request, 'index.html')
    