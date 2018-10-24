from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, SigninForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('posts:posts')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'membership/login_view.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:posts')
    else:
        pass


def signin_view(request):
    context = {}
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:posts')
    else:
        form = SigninForm()

    context['form'] = form
    return render(request, 'membership/signin_view.html', context)
