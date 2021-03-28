from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul': 'Percentage Char Function',
        'content': 'Percentage Function',
        'banner': 'about/img/banner_about.png',
        'app_css': 'about/css/styles.css'
    }
    return render(request, 'percentage/index.html', context)
