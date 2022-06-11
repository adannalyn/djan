from django.contrib import admin
from .models import People, Doctor, Address, Product
# Register your models here.

admin.site.register(People)
admin.site.register(Doctor)
admin.site.register(Address)
admin.site.register(Product)
