from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import UserForm# , # StudentSkillsForm # TODO: JobForm, MyUserCreationForm

from projects.models import File, ProjectTopic, Project, GradeReport, \
ProjectOfUser, Teacher, Student, Grade, ProjectMeeting, Meeting
from projects.serializers import *

from rest_framework import generics, permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешение только для владельца объекта на редактирование.
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешить любые безопасные (например, GET) запросы.
        return obj.owner == request.user  # Здесь obj.owner - это поле, содержащее владельца объекта.
    
@login_required
def home_page(request):
    # if request.user.is_superuser:
    #     return render(request, 'admin_page.html')
    if False:
        return render(request, 'moderator_page.html')
    elif False:
        return render(request, 'teacher_page.html')
    elif True:
        return render(request, 'base/student_page.html')
    else:
        return render(request, 'general_page.html')

# @login_required
def student_form(request):
    if request.method == 'POST':
        form = StudentSkillsForm(request.POST)
        print(form)
        if form.is_valid():
            student_name = form.cleaned_data['skill']
            student = Student.objects.create(name=student_name)
            student.save()
            return HttpResponse('Student was created with name ' + student.name)
    # логика формы для студентов
    form = StudentSkillsForm()
    context = {'form': form}
    return render(request, 'base/student_form.html', context)

# File
class FileListAPIView(generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class FileDestroyAPIView(generics.DestroyAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class FileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class FileCreateAPIView(generics.CreateAPIView):
   serializer_class = FileSerializer
   queryset = File.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# ProjectTopic
class ProjectTopicListAPIView(generics.ListAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ProjectTopicDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectTopicUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectTopicCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectTopicSerializer
   queryset = ProjectTopic.objects.all()
   permission_classes = [permissions.IsAdminUser] # TODO

# Project
class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer # ProjectDepthSerializer TODO:
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectSerializer
   queryset = Project.objects.all()
   permission_classes = [permissions.IsAdminUser]

# GradeReport
class GradeReportListAPIView(generics.ListAPIView):
    serializer_class = GradeReportSerializer # TODO: GradeReportDepthSerializer
    queryset = GradeReport.objects.all()
    permission_classes = [permissions.IsAdminUser]

class GradeReportDestroyAPIView(generics.DestroyAPIView):
    serializer_class = GradeReportSerializer
    queryset = GradeReport.objects.all()
    permission_classes = [permissions.IsAdminUser]

class GradeReportUpdateAPIView(generics.UpdateAPIView):
    serializer_class = GradeReportSerializer
    queryset = GradeReport.objects.all()
    permission_classes = [permissions.IsAdminUser]

class GradeReportCreateAPIView(generics.CreateAPIView):
   serializer_class = GradeReportSerializer
   queryset = GradeReport.objects.all()
   permission_classes = [permissions.IsAdminUser]

# ProjectOfUser
class ProjectOfUserListAPIView(generics.ListAPIView):
    serializer_class = ProjectOfUserSerializer # TODO: ProjectOfUserDepthSerializer
    queryset = ProjectOfUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectOfUserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectOfUserSerializer
    queryset = ProjectOfUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectOfUserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectOfUserSerializer
    queryset = ProjectOfUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProjectOfUserCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectOfUserSerializer
   queryset = ProjectOfUser.objects.all()
   permission_classes = [permissions.IsAdminUser]

# Teacher
class TeacherListAPIView(generics.ListAPIView):
    serializer_class = TeacherSerializer # TODO: TeacherDepthSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TeacherDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAdminUser]

class TeacherUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAdminUser]

class TeacherCreateAPIView(generics.CreateAPIView):
   serializer_class = TeacherSerializer
   queryset = Teacher.objects.all()
   permission_classes = [permissions.IsAdminUser]

# Student
class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer # TODO: StudentDepthSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class StudentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAdminUser]

class StudentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAdminUser]

class StudentCreateAPIView(generics.CreateAPIView):
   serializer_class = StudentSerializer
   queryset = Student.objects.all()
   permission_classes = [permissions.IsAdminUser]

# Grade
class GradeListAPIView(generics.ListAPIView):
    serializer_class = GradeSerializer # TODO: GradeDepthSerializer
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class GradeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class GradeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class GradeCreateAPIView(generics.CreateAPIView):
   serializer_class = GradeSerializer
   queryset = Grade.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# ProjectMeeting
class ProjectMeetingListAPIView(generics.ListAPIView):
    serializer_class = ProjectMeetingSerializer # TODO: ProjectMeetingDepthSerializer
    queryset = ProjectMeeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class ProjectMeetingDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectMeetingSerializer
    queryset = ProjectMeeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class ProjectMeetingUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectMeetingSerializer
    queryset = ProjectMeeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class ProjectMeetingCreateAPIView(generics.CreateAPIView):
   serializer_class = ProjectMeetingSerializer
   queryset = ProjectMeeting.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# Meeting
class MeetingListAPIView(generics.ListAPIView):
    serializer_class = MeetingSerializer # TODO: MeetingDepthSerializer
    queryset = Meeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class MeetingDestroyAPIView(generics.DestroyAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class MeetingUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

class MeetingCreateAPIView(generics.CreateAPIView):
   serializer_class = MeetingSerializer
   queryset = Meeting.objects.all()
   permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]

# Home
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    projects = Project.objects.filter(
        # Q(projectofuser__projecttopic__name__icontains=q) | TODO:
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    for project in projects: 
        project.__dict__['participant_count'] = ProjectOfUser.objects.filter(project_field=project).count()
        project.__dict__['participants'] = [match.user for match in ProjectOfUser.objects.filter(project_field=project)]

    topics = ProjectTopic.objects.all()[0:5]
    project_count = projects.count()
    project_meetings = ProjectMeeting.objects.filter(
        Q(name__icontains=q))[0:3] # Тут нужно по топику # TODO: 

    # project_to_teacher = get_project_to_teacher(projects)  
    # pc = ParticipantCount(projects)
    context = {'projects': projects, 
               # 'project_to_teacher': project_to_teacher, 
               'topics': topics,
               'project_count': project_count, 
               'project_meetings': project_meetings}
               # 'participant_count': pc}
    

    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = ProjectTopic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

def activityPage(request):
    project_meetings = ProjectMeeting.objects.all()
    return render(request, 'base/activity.html', {'project_meetings': project_meetings})