# from django.http import HttpResponse
# from django.conf import settings
# from django.contrib import admin
# from django.conf.urls.static import static
from django.conf.urls import url


from .import views

urlpatterns = [
    url(r'^$', views.post_new, name='new_blog_post'),
    url(r'^$', views.post_list, name='homepage'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='blogpost_single'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='edit_blogpost'),
    url(r'^drafts/$', views.post_draft_list, name='blogpost_draft'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
]

