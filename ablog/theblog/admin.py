from django.contrib import admin
from . models import post, Category, Profile, Comment

# Register your models here.

admin.site.register(post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)

