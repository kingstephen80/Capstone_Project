from django.db import models
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class BlogTopics(models.Model):
    topic = models.CharField(max_length=120)

    def __str__(self):
        return self.topic


class CreateNEW(models.Model):
    title = models.CharField(max_length=90)
    author = User.get_full_name
    date_created = models.DateTimeField(default=timezone.now)
    posted_date = models.DateTimeField(blank=True, null=True)
    main_text = models.TextField(max_length=5000, blank=True, null=True)
    topic = models.ForeignKey(BlogTopics)
    comments = models.TextField(max_length=366)

    def publish(self):
        self.posted_date = timezone.now
        self.save()

    def __str__(self):
        return self.title
