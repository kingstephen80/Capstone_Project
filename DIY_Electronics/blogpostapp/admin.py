from django.contrib import admin

from .models import BlogPost
from .models import GeneralTopics


class BlogPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogPost, BlogPostAdmin)


class GeneralTopicsAdmin(admin.ModelAdmin):
    pass
admin.site.register(GeneralTopics, GeneralTopicsAdmin)
