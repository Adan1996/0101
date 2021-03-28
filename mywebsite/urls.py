from django.conf.urls import url, include
from django.contrib import admin

from . import views
# from about import views as aboutViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^percentage_char/', include('percentage_char.urls')),
    url(r'^$', views.index),
]
