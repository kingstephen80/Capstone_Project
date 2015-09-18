# from django.http import HttpResponse
# from django.conf import settings
# from django.contrib import admin
# from django.conf.urls.static import static
from django.conf.urls import url


from .import views

urlpatterns = [
    url(r'^$', views.new_blog_post, name='new_blog_post'),
    url(r'^$', views.homepage, name='homepage'),
    # url(r'^$', views.post_list, name='post_list')
]
