from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    Room,
    Teacher,
    Discipline,
    Group,
    Student,
    TimeSlot,
    Schedule,
    Grade,
    UserRole,
)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["number", "capacity"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "room"]


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", "course"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "group"]


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ["day_of_week", "start_time", "end_time"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["group", "semester", "timeslot", "room", "discipline", "teacher"]


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["semester", "discipline", "student", "grade"]


class UserRoleInline(admin.StackedInline):
    model = UserRole
    can_delete = True


class UserAdmin(BaseUserAdmin):
    inlines = [UserRoleInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)