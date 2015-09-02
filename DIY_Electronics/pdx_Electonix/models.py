from django.db import models
from django.contrib.auth.models import User
# Create your models here.


__author__ = 'Stephen.king.pdx@gmail.com'



# The projects model is for the creation and viewing of Electronic Prototyping User projects.
# These can be viewed anytime and added to after user has been approved.
class Projects(models.Model):
    title = models.CharField(60)
    user = models.OneToOneField(User)
    date = models.DateTimeField
    difficulty = models.CharField(choices=)
    instructions = models.TextField(max_length=365)
    tool_list = models.CharField(max_length=180)
    parts_list = models.CharField(max_length=180)
    scripts_code = models.TextField(max_length=365)
    script_language = models.CharField(max_length=180)



# New user model.
# Following the information from:https://docs.djangoproject.com/en/1.8/topics/auth/customizing/
class Contributors(models.Model):
    user = models.OneToOneField(User)
    userName = models.CharField(max_length=20)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.EmailField(max_length=90)
    password =