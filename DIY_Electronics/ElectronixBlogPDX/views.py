from django.shortcuts import render_to_response, get_object_or_404, render
# from django.http import HttpResponse
# from django.core.urlresolvers import reverse
# from .models import CreateNEW, BlogTopics


def new_blog_post(request):
    return render('This is Your New Blog Page')


def homepage(request):
    return render(request, "Templates/homepage.html")
