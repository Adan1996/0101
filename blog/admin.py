from django.contrib import admin

# Register your models here.

from .models import Post
# or from . import models

# admin.site.register(models.Post)
admin.site.register(Post)