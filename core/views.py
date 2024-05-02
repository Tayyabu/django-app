import os
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, BlogPostForm
from .models import BlogPost
from django.db.models import Q
login_url='/login'
# Create your views here.
@login_required(login_url=login_url)
def home(request):
    
    is_home=True
    posts=BlogPost.objects.all()
    if request.method == 'POST':
        searched=request.POST.get('search')
        if searched is not None:
            posts=BlogPost.objects.filter(Q(title__icontains=searched)|Q(content__icontains=searched))
    return render(request, "index.html",{'posts':posts,'is_home':is_home})


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, f"You are logged in")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Failed to login! please  try again")
            return redirect("home")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.warning(request, f"You are logged out ")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect("home")
        else:
            for error in form.error_messages.values():
                messages.error(request, f"{error}")
            return redirect("register")

    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})


@login_required(login_url=login_url)
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("home")
        else:
            for error in form.error_messages.values():
                messages.error(request, f"{error}")

            return redirect("home")
    form = BlogPostForm()
    return render(request, "create_post.html", {"form": form})

@login_required(login_url=login_url)
def edit_post(request,pk):
    post =get_object_or_404(BlogPost,id=pk)
    if request.method=="POST":
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        if len(request.FILES) !=0: 
           if len(post.image) >0:
               os.remove(post.image.path)
           post.image=request.FILES.get('image')
        post.save()
        return redirect('home')
    return render(request,"edit_post.html",{"post":post})


@login_required(login_url=login_url)
def post_page(request,pk):
    post =get_object_or_404(BlogPost,id=pk)
    return render(request,'post_page.html',{'post':post})
def delete_post(request,pk):
    post =get_object_or_404(BlogPost,id=pk)
    post.delete()
    if len(post.image) >0:
        os.remove(post.image.path)
    return redirect('home')