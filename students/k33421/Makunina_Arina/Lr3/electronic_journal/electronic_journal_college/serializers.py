from rest_framework import serializers
from .models import Room, Teacher, Discipline, Group, TeachingAssignment, Student, TimeSlot, Schedule, Grade


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeachingAssignmentSerializer(serializers.ModelSerializer):
    discipline = DisciplineSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = TeachingAssignment
        fields = '__all__'


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    schedule = serializers.SerializerMethodField('get_schedule_info')

    class Meta:
        model = Grade
        fields = '__all__'

    def get_schedule_info(self, grade):
        schedule = grade.schedule
        return {
            'id': schedule.id,
            'discipline': schedule.discipline.name,
            'teacher': schedule.teacher.name,
        }


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
