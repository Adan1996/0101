from django.conf.urls import url, include
from django.contrib import admin

from . import views
from percentage_char.views import PercentageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^percentage_char/', PercentageView.as_view(template_name="percentage/index.html")),
]
