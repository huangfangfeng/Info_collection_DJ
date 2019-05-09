"""infocollection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from infocollection.view import index
#from collection import submit
from collection import admin
from collection import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', index),  #首页 选择页面
    url(r'collection', views.index),  #填写页面
    url(r'submit', views.submit),  #填写处理
    url(r'admin', admin.reflush),  #后台页面
]
