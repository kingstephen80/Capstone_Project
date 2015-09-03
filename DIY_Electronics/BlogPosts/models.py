from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    text_main = models.TextField(max_length=365)
    title = models.CharField(max_length=120)
    author = models.User
    date = models.DateTimeField
    topic = models.CharField(max_length=4)
    user_comments = models.TextField(max_length=365)
    # ID field

    def __unicode__(self):
        return self.author, self.date,


class GeneralTopics(models.Model):
    Arduino = 'Ar'
    RaspberryPi = 'RPi'
    Intel_Galileo = 'IG'
    Electronic_projects_Topics = (
        (Arduino, 'Arduino'),
        (RaspberryPi, 'RaspberryPi'),
        (Intel_Galileo, 'Intel_Galileo'),
    )
    electronic_project_topics = models.CharField(max_length=3, choices=Electronic_projects_Topics, default=Arduino)

    def __unicode__(self):
        return self.name
