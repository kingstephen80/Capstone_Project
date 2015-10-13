
from django.forms import ModelForm
from .models import NewPost, BlogTopics


class BlogForm(ModelForm):
    class Meta:
        model = NewPost
        fields = ('title', 'main_text')


class TopicsForm(ModelForm):
    class Meta:
        model = BlogTopics
        fields = '__all__'



# 10-3-15_8:30pm
# changed import location from django to django.forms and forms.Model to ModelForm. The change was inspired out of  reading the djangoDocs.
#
#
#
#