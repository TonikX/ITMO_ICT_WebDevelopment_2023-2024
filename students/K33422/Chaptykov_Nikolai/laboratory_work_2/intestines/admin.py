from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from intestines.models import Student, Teacher, Homework, Discipline, AssignedHomework, StudentPerformance, StudentGrade, SchoolGroup
# Register your models here.


class StudentInLine(admin.StackedInline):
	model = Student
	verbose_name_plural = 'Students'
	can_delete = False


class TeacherInLine(admin.StackedInline):
	model = Teacher
	verbose_name_plural = 'Students'
	can_delete = False


class CustomizedUserAdmin(UserAdmin):
	inlines = (TeacherInLine, StudentInLine)


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(Discipline)
admin.site.register(AssignedHomework)
admin.site.register(StudentPerformance)
admin.site.register(StudentGrade)
admin.site.register(SchoolGroup)