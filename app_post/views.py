from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, PostForm
from .models import BlogPost

# --------------------------------Login and Register Views-------------------------------


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registered Successfully!")
                return redirect('login')
        context = {"form": form}
        return render(request, 'app_post/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect ")
        context = {}

        return render(request, 'app_post/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# --------------------------------------Other Views-------------------------------------


@login_required(login_url='login')
def home(request):

    posts = BlogPost.objects.all()
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'app_post/home.html', context)


def write(request):
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'app_post/write.html', context)


def post_detail(request, pk):
    post = BlogPost.objects.get(id=pk)
    context = {
        "post": post
    }
    return render(request, 'app_post/post_detail.html', context)


def post_edit(request, pk):
    post = BlogPost.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'app_post/post_edit.html', context)


def post_delete(request, pk):
    post = BlogPost.objects.get(id=pk)
    post.delete()
    return redirect('home')
