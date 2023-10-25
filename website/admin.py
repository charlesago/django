from django.contrib import admin
from .models import Message, User, Category, Response

# Register your models here.

admin.site.register(Message)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Response)