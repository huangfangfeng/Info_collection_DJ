# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from collection.models import collection

# Create your views here.
def index(request):
     return render(request, 'collection.html')
     

def submit(request):
    request.encoding = 'utf-8'
    message = ''
    for key in request.GET:
        if request.GET[key] == '':
            message = '请填写完整信息'
            break
    if 'nameinfo' in request.GET and message == '':
        message = "OK" 
        test1 = collection(nameinfo = request.GET['nameinfo'], sex = request.GET['sex'], num = request.GET['num'], tel = request.GET['tel'], email = request.GET['email'], wechat = request.GET['wechat'], addr = request.GET['addr'], position = request.GET['position'], sport = request.GET['sport'], food = request.GET['food'])
        test1.save()
    return render(request, 'transition.html',{"message":message})
    #return HttpResponse(message)