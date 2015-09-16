from django.contrib import admin

from .models import BlogTopics
from .models import CreateNEW


class CreateNEWAdmin(admin.ModelAdmin):
    pass
admin.site.register(CreateNEW, CreateNEWAdmin)


class BlogTopicsAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogTopics, BlogTopicsAdmin)
