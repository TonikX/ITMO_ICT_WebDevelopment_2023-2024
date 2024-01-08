from rest_framework import serializers
from .models import *


''' 
User Serializers
'''

class UserSerializer(serializers.ModelSerializer):
  class Meta:
     model = User
     fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
     model = User
     fields = "__all__"


'''
Courses Serializers
'''

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
     model = Course
     fields = "__all__"


class CourseSubjectsSerializer(serializers.ModelSerializer):
   class Meta:
     model = Subject
     fields = ('name', 'about_info', 'thumbnail')


class CourseDetailSerializer(serializers.ModelSerializer):
  subjects = CourseSubjectsSerializer(many=True, read_only=True)

  class Meta:
     model = Course
     fields = ('name', 'about_info', 'thumbnail', 'subjects')


class CourseStudentSerializer(serializers.ModelSerializer):
   class Meta:
      model = CourseStudent
      fields = "__all__"


class CourseTeacherSerializer(serializers.ModelSerializer):
   class Meta:
      model = CourseTeacher
      fields = "__all__"


class CourseCreateSerializer(serializers.ModelSerializer):
  class Meta:
     model = Course
     fields = "__all__"


''' 
Subjects Serializers
'''

class SubjectLessonsSerializer(serializers.ModelSerializer):
   class Meta:
     model = Lesson
     fields = ('name', 'content', 'thumbnail')


class SubjectDetailSerializer(serializers.ModelSerializer):
  lessons = SubjectLessonsSerializer(many=True, read_only=True)

  class Meta:
     model = Subject
     fields = ('name', 'about_info', 'thumbnail', 'lessons')


class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
     model = Subject
     fields = "__all__"


class SubjectCreateSerializer(serializers.ModelSerializer):
  class Meta:
     model = Subject
     fields = "__all__"


''' 
Lessons Serializers
'''

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
     model = Lesson
     fields = "__all__"


class LessonCreateSerializer(serializers.ModelSerializer):
  class Meta:
     model = Lesson
     fields = "__all__"


''' 
Applications Serializers
'''

class ApplicationSerializer(serializers.ModelSerializer):
  class Meta:
     model = Application
     fields = "__all__"


class ApplicationCreateSerializer(serializers.ModelSerializer):
  class Meta:
     model = Application
     fields = ('course', 'user', 'apply_message')


class ApplicationReviewSerializer(serializers.ModelSerializer):
  class Meta:
     model = Application
     fields = "__all__"