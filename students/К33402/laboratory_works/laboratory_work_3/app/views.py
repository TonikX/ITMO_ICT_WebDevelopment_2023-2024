from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Teacher, LessonTeacher, Lesson, Schedule, Student, StudentClass, Mark, Room
from . import serializers
import datetime
from rest_framework.permissions import IsAuthenticated


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    @action(detail=False, methods=['GET'])
    def count_base(self, request):
        count = Room.objects.filter(base=True).count()
        return Response({"base": count})

    @action(detail=False, methods=['GET'])
    def count_specific(self, request):
        count = Room.objects.filter(base=False).count()
        return Response({"specific": count})


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

    @action(detail=True, methods=['GET'])
    def other_teachers(self, request, pk=None):
        obj = self.get_object()
        qs = Lesson.objects.filter(who_teach__in=LessonTeacher.objects.filter(teacher=obj.id)).distinct()
        ser = serializers.ShowOtherTeachersSerializers(qs, many=True)
        return Response(ser.data)


class LessonTeacherViewSet(viewsets.ModelViewSet):
    queryset = LessonTeacher.objects.all()
    serializer_class = serializers.LessonTeacherSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

    @action(detail=False, methods=['GET'])
    def how_many_teachers(self, request):
        print(request)
        ser = serializers.CountTeachersSerializer(self.queryset, many=True)
        return Response(ser.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = serializers.StudentClassSerializer

    @action(detail=True, methods=["GET"])
    def count_boys_and_girls(self, request, pk=None):
        obj = self.get_object()
        ser = serializers.CountBGClassSerializer(obj)
        return Response(ser.data)

    @action(detail=True, methods=["GET"])
    def statistics(self, request, pk=None):
        students = Student.objects.filter(student_class=pk)
        ser = serializers.ShowStatlessonSerializer(Lesson.objects.all(), many=True, context={"students": students})
        return Response(ser.data)


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()

    def get_serializer_class(self):
        if self.action == "find":
            return serializers.FindScheduleSerializer
        return serializers.ScheduleSerializer

    @action(detail=False, methods=['POST'])
    def find(self, request):
        day = request.data.get("day", None)
        num_lesson = request.data.get("num_lesson", None)
        room = request.data.get("room", None)

        qs = self.queryset.filter(num_lesson=num_lesson, day=day, room=room.id)
        ser = serializers.ScheduleSerializer(qs, many=True)

        return Response(ser.data)

