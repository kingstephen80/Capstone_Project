from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from .import views

urlpatterns = [
    # url(r'^$', views.newblogpost, name='newblogpost'),
    url(r'^$', views.homepage, name='homepage'),
]

