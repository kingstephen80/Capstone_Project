
from django.forms import ModelForm
from .models import NewPost, BlogTopics


class BlogForm(ModelForm):
    class Meta:
        models = NewPost
        fields = '__all__'


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