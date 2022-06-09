from inspect import ArgInfo
from django.contrib import admin
from .models import Article,Like
# Register your models here.


admin.site.register(Article)
admin.site.register(Like)