from django.contrib import admin
from .models import Post # to showcase the model in the admin panel

# Register your models here.
admin.site.register(Post)