
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.new_blog_post, name='new_blog_post'),
    url(r'^Templates/$', views.blogposts_all, name='blogposts_all'),
    url(r'^blogpost/single/(?P<pk>[0-9]+)/$', views.blogpost_single, name='blogpost_single'),
    url(r'^edit/blogpost/(?P<pk>[0-9]+)/blogpost_single/$', views.edit_blogpost, name='edit_blogpost'),
    url(r'^blogpost/draft/$', views.blogpost_draft, name='blogpost_draft'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
]
