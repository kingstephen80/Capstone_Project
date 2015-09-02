from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class BlogPost(models.Model):
    text_main = models.TextField(max_length=365)
    author = models.User
    date = models.DateTimeField
    topic = models.CharField(max_length=4, choices=,,)
    user_comments = models.TextField(max_length=130)

class ProjectsTopics(models.Model):
    Arduino = 'Ar'
    RaseberryPi = 'RPi'
    Intel_Galileo = 'IG'
    Electronic_projects_Topics = (
        (Arduino, 'Ardunio')
        (RaseberryPi, 'RaseberryPi')
        (Intel_Galileo, 'Intel_Galileo'),
    )
    electronic_project_topics = models.CharField(max_length=3,
                                                 choices=Electronic_projects_Topics,default=Arduino)

