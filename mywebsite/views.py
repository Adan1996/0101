from django.shortcuts import render

# method view


def index(request):
    context = {
        'judul': 'Home',
        'content': 'Welcome to my website',
        'banner': 'img/banner_home.png'
    }
    return render(request, 'index.html', context)
