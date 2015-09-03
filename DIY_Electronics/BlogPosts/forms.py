# __author__ = 'stephen.king.pdx@gmail.com'

from django import forms
from .models import BlogPost, GeneralTopics


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost



class TopicSelect(forms.ModelForm):
    class Meta:
        model = GeneralTopics
