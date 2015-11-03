
from django import forms

from .models import NewPost, BlogTopics


class BlogForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('title', 'main_text',)


class TopicsForm(ModelForm):
    class Meta:
        model = BlogTopics
        fields = '__all__'



# 10-3-15_8:30pm
# changed import location from django to django.forms and forms.Model to ModelForm. The change was inspired out of  reading the djangoDocs.
#
#10-25-15_ 2220hrs
#returned to the original, import here; from django import forms and class BlogForm(forms.ModelForm):
#