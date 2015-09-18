from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.urlresolvers import reverse
from .models import CreateNEW


def homepage(request):
    # wanting to have the latest post. query the database looking for the one with the most recent date
    # for most_recent in CreateNEW.objets.all():
    #     return CreateNEW.object.latest('posted_date')
    return render(request, './homepage.html')


def new_blog_post(request):
    return render(request, './new_blog_post.html')
