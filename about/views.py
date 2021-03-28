from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul': 'About',
        'content': 'This is About page',
        'banner': 'about/img/banner_about.png',
        'app_css': 'about/css/styles.css'
    }
    return render(request, 'about/index.html', context)
