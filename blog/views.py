from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    # queryset
    posts = Post.objects.all()

    context = {
        'judul': 'Blog Page',
        'content': 'This blog has been created from blog folder',
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'Category': 'All',
        'Posts': posts
    }
    return render(request, 'blog/index.html', context)

def jurnal(request):
    # queryset
    posts = Post.objects.filter(category='jurnal')

    context = {
        'judul': 'Blog Page',
        'content': 'This blog has been created from blog folder',
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'Category': 'Jurnal',
        'Posts': posts
    }
    return render(request, 'blog/index.html', context)

def berita(request):
    # queryset
    posts = Post.objects.filter(category='berita')

    context = {
        'judul': 'Blog Page',
        'content': 'This blog has been created from blog folder',
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'Category': 'Berita',
        'Posts': posts
    }
    return render(request, 'blog/index.html', context)

def gosip(request):
    # queryset
    posts = Post.objects.filter(category='gosip')

    context = {
        'judul': 'Blog Page',
        'content': 'This blog has been created from blog folder',
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'Category': 'Gosip',
        'Posts': posts
    }
    return render(request, 'blog/index.html', context)