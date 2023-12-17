from django.contrib import admin
from .models import User, TaskUserRelation, Task, Category, Aim, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


@admin.register(TaskUserRelation)
class TaskUserRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'category', 'aim', 'deadline')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Aim)
class AimAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'date_start', 'date_end')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'task_user_relation')

