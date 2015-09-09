from django.db import models

# Create your models here.


# New user model.
# Following the information from:https://docs.djangoproject.com/en/1.8/topics/auth/customizing/
class Contributors(models.Model):
    user = models.OneToOneField(User)
    userName = models.CharField(max_length=20)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.EmailField(max_length=90)
    password =