
from django import forms
from .models import BlogTopics, CreateNEW


class CreateNEW(forms.ModelForm):
    class Meta:
        models = CreateNEW
        fields = '__all__'


class CreateNEW(forms.ModelForm):
    class Meta:
        model = BlogTopics
        fields = '__all__'
