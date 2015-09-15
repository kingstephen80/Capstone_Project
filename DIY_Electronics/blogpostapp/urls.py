from django.http import HttpResponse
from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.newblogpost, name='newblogpost')
]

