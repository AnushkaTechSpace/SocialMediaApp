from django.shortcuts import render,redirect,get_object_or_404
from .models import User, Post, Like, Comment
# from django.contrib.auth import authenticate,login as auth_login
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError
from .forms import SearchForm,UserRegistrationForm,PostForm,CommentForm
from django.contrib.auth import login
# from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    return render(request,'home.html')

# @csrf_protect
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user) 
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)  
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials')
#     return render(request, 'login.html')


def post(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post.html', {'posts': posts})

def search(request):
    form = SearchForm()
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(content__icontains=query)
    
    return render(request, 'search.html', {
        'form': form,
        'results': results
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post')
    return render(request, 'delete_post.html', {'post': post})

def posts_view(request):
    posts = Post.objects.all()
    user_likes = {post.id: post.like_set.filter(user=request.user).exists() for post in posts}
    return render(request, 'post.html', {
        'posts': posts,
        'user_likes': user_likes,
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Unlike if already liked
    return redirect('post')

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('post')