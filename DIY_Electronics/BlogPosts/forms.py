# __author__ = 'stephen.king.pdx@gmail.com'

from django import forms
from .models import BlogPost, GeneralTopics


class BlogCreateNEW(forms.ModelForm):
    class Meta:
        models = BlogPost
        fields = '__all__'


class SelectTopic(forms.ModelForm):
    class Meta:
        model = GeneralTopics
        fields = '__all__'
