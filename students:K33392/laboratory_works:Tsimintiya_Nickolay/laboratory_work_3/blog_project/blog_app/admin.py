from django.contrib import admin
from .models import Post, Comment, Subscriptions

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subscriptions)
# Register your models here.
