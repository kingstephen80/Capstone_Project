
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from .models import NewPost
from .forms import BlogForm


def blogposts_all(request):
    posts = NewPost.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    return render(request, 'blogposts_all.html', {'posts': posts})


def blogpost_single(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    return render(request, 'blogpost_single.html', {'post': post})


@login_required
def new_blog_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 10-19-15_2115: changed out date_published to posted_dated. date_published is from a tutorial I was
            # working through.
            post.posted_date = timezone.now()
            post.save()
            return redirect('electronix_pdx.views.blogpost_single', pk=post.pk)
    else:
        form = BlogForm()
    return render(request, 'electronix_pdx/edit_blogpost.html', {'form': form})


@login_required
def edit_blogpost(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.posted_date = timezone.now()
            # 10-19-15_2120: changed out date_published to posted_dated. date_published is from a tutorial I was
            # working through.
            post.save()
            return redirect('electronix_pdx.views.blogpost_single', pk=post.pk)

    else:
        form = BlogForm(instance=post)
    return render(request, 'edit_blogpost.html', {'form': form})


@login_required
def blogpost_draft(request):
    posts = NewPost.objects.filter(posted_date__isnull=True).order_by('date_created')
    return render(request, 'blogpost_draft.html', {'post': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    post.publish()
    return redirect('electronix_pdx.views.blogpost_single', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    post.delete()
    return redirect('electronix_pdx.views.blogposts_all')
