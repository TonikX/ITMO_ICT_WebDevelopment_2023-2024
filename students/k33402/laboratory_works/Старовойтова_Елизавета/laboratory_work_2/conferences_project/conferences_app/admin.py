from django.contrib import admin
from .models import UserProfile, Conference, AuthorRegistration, Comment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'surname', 'lastname', 'passport']
    search_fields = ['user__username', 'surname', 'lastname', 'passport']

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location']
    search_fields = ['name', 'location']

@admin.register(AuthorRegistration)
class AuthorRegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'conference', 'date_registered']
    search_fields = ['user__username', 'conference__name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'conference', 'date_created', 'rating']
    search_fields = ['user__username', 'conference__name']
