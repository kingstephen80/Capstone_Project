from django.contrib import admin

from .models import BlogTopics
from .models import NewPost


class NewPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(NewPost)


class BlogTopicsAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogTopics, BlogTopicsAdmin)
