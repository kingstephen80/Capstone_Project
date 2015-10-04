
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import NewPost
from .forms import BlogForm


def post_list(request):
    posts = NewPost.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, "Templates/homepage.html", {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    return render(request, "Templates/blogpost_single.html", {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect('electronix_pdx.views.post_detail', pk=post.pk)
    else:
        form = BlogForm()
    return render(request, 'Templates/edit_blogpost.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect('electronix_pdx.views.post_detail', pk=post.pk)

    else:
        form = BlogForm(instance=post)
    return render(request, 'Templates/edit_blogpost.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = NewPost.objects.filter(date_published__isnull=True).order_by('date_created')
    return render(request, 'Templates/blogpost_draft.html', {'post': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    post.publish()
    return redirect('electronix_pdx.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    post.delete()
    return redirect('electronix_pdx.views.homepage')
