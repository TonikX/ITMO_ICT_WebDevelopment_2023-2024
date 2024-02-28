from rest_framework import serializers
from projects.models import File, ProjectTopic, Project, GradeReport, \
ProjectOfUser, Teacher, Student, Grade, ProjectMeeting, Meeting

class FileSerializer(serializers.ModelSerializer):
  class Meta:
     model = File
     fields = "__all__"

class ProjectTopicSerializer(serializers.ModelSerializer):
  class Meta:
     model = ProjectTopic
     fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
     model = Project
     fields = "__all__"

class ProjectDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = "__all__"

    depth = 1

class GradeReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = GradeReport
    fields = "__all__"

class GradeReportDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = GradeReport
    fields = "__all__"

    depth = 1

class ProjectOfUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectOfUser
    fields = "__all__"

class ProjectOfUserDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectOfUser
    fields = "__all__"

    depth = 1

class TeacherSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Teacher
    fields = "__all__"

class TeacherDepthSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Teacher
    fields = "__all__"

    depth = 1

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__"

class StudentDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__"

    depth = 1

class GradeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = "__all__"

class GradeDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = "__all__" 

    depth = 1

class ProjectMeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMeeting
    fields = "__all__"

class ProjectMeetingDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMeeting
    fields = "__all__"

    depth = 1

class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = "__all__"

class MeetingDepthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = "__all__"

    depth = 1