# from django import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse


def homepage(request):
    if request.method == 'GET':
        return request, 'homepage.html'
