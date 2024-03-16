import datetime
from rest_framework import serializers
from .models import Teacher, LessonTeacher, Lesson, Schedule, StudentClass, Student, Mark, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CountTeachersSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['name', 'count']

    def get_count(self, obj):
        return LessonTeacher.objects.filter(lesson=obj.id).count()


class ShowOtherTeachersSerializers(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['name', 'teachers']

    def get_teachers(self, obj):
        teachers_qs = Teacher.objects.filter(what_teach__in=LessonTeacher.objects.filter(lesson=obj.id)).distinct()
        ser = TeacherSerializer(teachers_qs, many=True)
        return ser.data


class LessonTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTeacher
        fields = "__all__"


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ShowStatlessonSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['name', 'students']

    def get_students(self, obj):
        sts = self.context["students"]
        res = {}
        for st in sts:
            res[st.name] = {'marks': [], "mean": 0.0}
            res[st.name]['marks'] = []
            for mark in Mark.objects.filter(schedule__lesson_teacher__lesson=obj.id, student=st.id):
                res[st.name]['marks'].append(mark.mark)

            if len(res[st.name]['marks']):
                res[st.name]['mean'] = sum(res[st.name]['marks'])/len(res[st.name]['marks'])
        return res


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = "__all__"


class CountBGClassSerializer(serializers.ModelSerializer):
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()

    class Meta:
        model = StudentClass
        fields = ['year', 'letter', 'boys', 'girls']

    def get_boys(self, obj):
        return Student.objects.filter(student_class=obj.id, sex='m').count()

    def get_girls(self, obj):
        return Student.objects.filter(student_class=obj.id, sex='f').count()


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class FindScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['day', 'num_lesson', 'room']


class ShowScheduleSerializer(serializers.ModelSerializer):
    lesson = serializers.CharField(source='lesson_teacher.lesson.name')
    teacher = serializers.CharField(source='lesson_teacher.teacher.name')

    class Meta:
        model = Schedule
        fields = ['day', 'num_lesson', 'room', 'student_class', 'lesson', 'teacher']

