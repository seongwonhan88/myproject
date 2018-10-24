from django.shortcuts import render, redirect

from .models import Post
from .forms import PostCreateForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_create(request):
    context = {}
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(author=request.user)
            return redirect('posts:posts')
    else:
        form = PostCreateForm()
    context['form'] = form
    return render(request, 'posts/post_create.html', context)
