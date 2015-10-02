
from django import forms
from .models import NewPost, BlogTopics


class BlogForm(forms.ModelForm):
    class Meta:
        models = NewPost
        fields = '__all__'


class TopicsForm(forms.ModelForm):
    class Meta:
        model = BlogTopics
        fields = '__all__'
