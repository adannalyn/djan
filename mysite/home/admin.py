from django.contrib import admin
from .models import Post, OurCustomer, Profile
# Register your models here.

admin.site.register(Post)

admin.site.register(OurCustomer)

admin.site.register(Profile)