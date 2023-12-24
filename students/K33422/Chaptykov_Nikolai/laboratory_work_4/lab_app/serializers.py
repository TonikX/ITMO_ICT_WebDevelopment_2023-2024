from lab_app.models import *
from rest_framework import serializers


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('time', 'discipline')


class AssignedLectureSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(many=True, read_only=True)
    group_str = serializers.StringRelatedField(source='group')

    class Meta:
        model = AssignedLecture
        fields = ('group', 'group_str', 'lecture')


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'group']


class StudentCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'group']


class AcademicPerformanceSerializer(serializers.ModelSerializer):
    student_str = serializers.StringRelatedField(source='student')
    subject_str = serializers.StringRelatedField(source='subject')

    class Meta:
        model = AcademicPerformance
        fields = ['student', 'student_str', 'subject', 'subject_str', 'grade']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicGroup
        fields = ('__all__')
