from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post) # to give admin all access to the post model , add, update,delete