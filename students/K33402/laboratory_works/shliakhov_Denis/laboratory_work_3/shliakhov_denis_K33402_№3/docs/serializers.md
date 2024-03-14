# Класс serializers.py    
    from rest_framework import serializers
    
    from .models import *
    
## TeacherSerializer    
    class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
            model = Teacher
            fields = '__all__'
    
## GroupSerializer    
    class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = '__all__'
    
## GradeSerializer     
    class GradeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Grade
            fields = '__all__'
    
## StudentSerializer    
    class StudentSerializer(serializers.ModelSerializer):
        grade_set = GradeSerializer(many=True)
    
        class Meta:
            model = Student
            fields = '__all__'
    
## CreateStudentSerializer    
    class CreateStudentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            fields = '__all__'
    
## TeachProcessSerializer    
    class TeachProcessSerializer(serializers.ModelSerializer):
        class Meta:
            model = TeachProcess
            fields = '__all__'
    
## SubjectSerializer    
    class SubjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = Subject
            fields = '__all__'
    
## LessonSerializer    
    class LessonSerializer(serializers.ModelSerializer):
        class Meta:
            model = Lesson
            fields = '__all__'
