from django.db import models

from django.utils import timezone


class BlogTopics(models.Model):
    topic = models.CharField(max_length=120)

    def __str__(self):
        return self.topic


class NewPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=90)
    topic = models.ForeignKey(BlogTopics)
    main_text = models.TextField(max_length=5000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    posted_date = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(max_length=366)

    def publish(self):
        self.posted_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
