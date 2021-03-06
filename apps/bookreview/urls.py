"""login_and_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
 	url(r'^books$', views.books),
    url(r'^add$', views.add),
    url(r'^newbook$', views.newbook),
    url(r'^logout$', views.logout), 
    url(r'^books/(?P<id>[0-9]+)/$', views.showbook),
    url(r'^newreview/(?P<id>[0-9]+)/$', views.newreview),
    url(r'^users/(?P<id>[0-9]+)/$', views.showuser),
    url(r'^delete/(?P<id>[0-9]+)/$', views.deletereview), 
]
