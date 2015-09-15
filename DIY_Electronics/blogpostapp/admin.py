from django.contrib import admin

from .models import CreateBlogPost
from .models import GeneralTopics


class BlogPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(CreateBlogPost, BlogPostAdmin)


class GeneralTopicsAdmin(admin.ModelAdmin):
    pass
admin.site.register(GeneralTopics, GeneralTopicsAdmin)
