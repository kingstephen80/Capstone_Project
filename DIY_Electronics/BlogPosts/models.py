from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    author = User
    date = models.DateTimeField(auto_now_add=True)
    text_main = models.TextField
    topic = models.CharField(max_length=4)
    user_comments = models.TextField(max_length=365)


# class Meta:
#         ordering = ['-created']

    def __unicode__(self):
            return u'%s'%self.title,

        # def get_absolute_url(self):
        #     return reverse('BlogPost.views.post', args=[self.slug])


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
