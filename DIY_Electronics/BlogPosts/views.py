from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import BlogPost, GeneralTopics
from .forms import BlogCreateForm, TopicSelect


def new_blog_post(request, list_id):
    newblogpost = get_object_or_404(new_blog_post, pk=list_id)
    header = 'Write Your NEW Blog Post Here!'.format(
        new_blog_post
    )

    if request.method == 'POST':
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            form.save(BlogCreateForm)
            return HttpResponseRedirect(reverse('Your BlogPost has been Published', args=[list_id]))

        else:
            form = BlogCreateForm()

        return render(request, 'BlogPostNew.html',{

            'form': form,
            'header': header
        },
    )
