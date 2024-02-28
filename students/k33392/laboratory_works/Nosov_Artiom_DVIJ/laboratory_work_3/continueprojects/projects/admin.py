from django.contrib import admin

# Register your models here.
from projects.models import User, File, ProjectTopic, Project, GradeReport, \
ProjectOfUser, Teacher, Student, Grade, ProjectMeeting, Meeting

admin.site.register(User)
admin.site.register(File)
admin.site.register(ProjectTopic)
admin.site.register(Project)
admin.site.register(GradeReport)
admin.site.register(ProjectOfUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(ProjectMeeting)
admin.site.register(Meeting)

