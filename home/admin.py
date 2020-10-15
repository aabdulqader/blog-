from django.contrib import admin
from .models import Post, Contact, Category, Profile

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Profile)