from datetime import datetime
from typing import Any, Dict

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from .models import Teacher, Student, Grade, TimeSlot, Discipline, Schedule, Room, Group


class UserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user

        return Response({"role": user.role.get_role_display() if hasattr(user, "role") else None})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.auth:
            request.auth.delete()
            return Response({"detail": "Вы успешно вышли из системы."}, status=status.HTTP_200_OK)
        return Response({"detail": "Нет информации об аутентификации."}, status=status.HTTP_400_BAD_REQUEST)


class TeacherView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        teacher_id = int(request.query_params.get("id")) if request.query_params.get("id") else None
        teacher_name = request.query_params.get("name")

        teacher_query = Teacher.objects

        if teacher_id:
            teacher_query = teacher_query.filter(id=teacher_id)
        if teacher_name:
            teacher_query = teacher_query.filter(name=teacher_name)

        teacher: Teacher = teacher_query.first()
        if not teacher:
            return Response({"error": "Teacher does not exist!"}, status.HTTP_404_NOT_FOUND)

        schedules = teacher.schedules.order_by("semester", "timeslot__day_of_week", "timeslot__start_time").all()
        formatted_schedule = {"semester": {}}

        for schedule in schedules:
            if schedule.semester not in formatted_schedule["semester"]:
                formatted_schedule["semester"][schedule.semester] = {}

            day_of_week = schedule.timeslot.get_day_of_week_display()
            if day_of_week not in formatted_schedule["semester"][schedule.semester]:
                formatted_schedule["semester"][schedule.semester][day_of_week] = []

            formatted_schedule["semester"][schedule.semester][day_of_week].append(
                {
                    "start_time": schedule.timeslot.start_time,
                    "end_time": schedule.timeslot.end_time,
                    "room": schedule.room.number,
                    "discipline": schedule.discipline.name,
                    "group": schedule.group.name,
                }
            )

        return Response(
            {
                "id": teacher.id,
                "name": teacher.name,
                "room": teacher.room.number,
                "disciplines": list(teacher.schedules.values_list("discipline__name", flat=True)),
                "schedule": formatted_schedule,
            }
        )

    def put(self, request: Request):
        teacher_id = int(request.query_params.get("id")) if request.query_params.get("id") else None
        teacher_name = request.query_params.get("name")

        teacher_query = Teacher.objects

        if teacher_id:
            teacher_query = teacher_query.filter(id=teacher_id)
        if teacher_name:
            teacher_query = teacher_query.filter(name=teacher_name)

        teacher: Teacher = teacher_query.first()
        if not teacher:
            return Response({"error": "Teacher does not exist!"}, status.HTTP_404_NOT_FOUND)

        data: dict[str, Any] = request.data
        new_name = data.get("name")
        new_room_id = data.get("room_id")

        if new_name:
            teacher.name = new_name
        if new_room_id:
            teacher.room_id = new_room_id

        teacher.save()

        return Response({"status": "success"})

    def delete(self, request: Request):
        teacher_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        teacher_query = Teacher.objects

        if teacher_id:
            teacher_query = teacher_query.filter(id=teacher_id)
        else:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        teacher: Teacher = teacher_query.first()
        if not teacher:
            return Response({"error": "Teacher does not exist!"}, status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return Response({"status": "success"})

    def post(self, request: Request):
        data = request.data
        teacher_name = data.get("name")
        if not teacher_name:
            return Response({"error": "'name' is required field"}, status.HTTP_400_BAD_REQUEST)

        room_id = data.get("room_id")

        teacher = Teacher(name=teacher_name, room_id=room_id)
        teacher.save()

        return Response({"status": "success"})


class TeachersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        teachers = list(Teacher.objects.values("id", "name", "room_id", "room__number"))

        return Response({"teachers": teachers})


class StudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        student_id = int(request.query_params.get("id")) if request.query_params.get("id") else None
        student_name = request.query_params.get("name")

        student_query = Student.objects

        if student_id:
            student_query = student_query.filter(id=student_id)
        if student_name:
            student_query = student_query.filter(name=student_name)

        student: Student = student_query.first()
        if not student:
            return Response({"error": "Student does not exist!"}, status.HTTP_404_NOT_FOUND)

        schedules = student.group.schedules.all()
        grades = student.grades.order_by("semester")

        formatted_grades = {"semester": {}}

        for schedule in schedules:
            if schedule.semester not in formatted_grades["semester"]:
                formatted_grades["semester"][schedule.semester] = {schedule.discipline.name: None}
            else:
                formatted_grades["semester"][schedule.semester][schedule.discipline.name] = None

        for grade in grades:
            if grade.semester not in formatted_grades["semester"]:
                formatted_grades["semester"][grade.semester] = {
                    grade.discipline.name: {"grade_id": grade.id, "grade_value": grade.grade}
                }
            else:
                formatted_grades["semester"][grade.semester][grade.discipline.name] = {
                    "grade_id": grade.id,
                    "grade_value": grade.grade,
                }

        return Response(
            {
                "id": student.id,
                "name": student.name,
                "group": student.group.name,
                "course": student.group.course,
                "grades": formatted_grades,
            }
        )

    def put(self, request: Request):
        student_id = int(request.query_params.get("id")) if request.query_params.get("id") else None
        student_name = request.query_params.get("name")

        student_query = Student.objects

        if student_id:
            student_query = student_query.filter(id=student_id)
        if student_name:
            student_query = student_query.filter(name=student_name)

        student: Student = student_query.first()
        if not student:
            return Response({"error": "Student does not exist!"}, status.HTTP_404_NOT_FOUND)

        data: dict[str, Any] = request.data
        new_name = data.get("name")
        new_group_id = data.get("group_id")

        if new_name:
            student.name = new_name
        if new_group_id:
            student.group_id = new_group_id

        student.save()

        return Response({"status": "success"})

    def delete(self, request: Request):
        student_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        student_query = Student.objects

        if student_id:
            student_query = student_query.filter(id=student_id)
        else:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        student: Student = student_query.first()
        if not student:
            return Response({"error": "Student does not exist!"}, status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({"status": "success"})

    def post(self, request: Request):
        data = request.data
        student_name = data.get("name")
        if not student_name:
            return Response({"error": "'name' is required field"}, status.HTTP_400_BAD_REQUEST)

        group_id = data.get("group_id")

        student = Student(name=student_name, group_id=group_id)
        student.save()

        return Response({"status": "success"})


from django.db.models import Avg, Func


class AbsAvg(Func):
    function = 'ABS'
    arity = 1


class GroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        group = request.query_params.get("group_name")
        course = request.query_params.get("course")
        discipline = request.query_params.get("discipline")
        teacher = request.query_params.get("teacher")

        students_query = Student.objects.order_by("group__course", "group__name")

        if group:
            students_query = students_query.filter(group__name=group)
        if course:
            students_query = students_query.filter(group__course=course)
        if discipline:
            students_query = students_query.filter(group__schedules__discipline__name=discipline)
        if teacher:
            students_query = students_query.filter(group__schedules__teacher__name=teacher)

        student_by_groups = {"groups": {}}
        for student in students_query:
            if student.group.name not in student_by_groups["groups"]:
                student_by_groups["groups"][student.group.name] = {
                    "course": student.group.course,
                    "students": [],
                    "students_count": 0,
                    "average_grade": None,
                }

            student_by_groups["groups"][student.group.name]["students"].append({"id": student.id, "name": student.name})
            student_by_groups["groups"][student.group.name]["students_count"] += 1

        for group_name, group_data in student_by_groups["groups"].items():
            group_students = Student.objects.filter(group__name=group_name)
            average_grade = group_students.aggregate(average_grade=Avg('grades__grade'))['average_grade']
            average_grade_rounded = round(abs(average_grade),
                                          2) if average_grade is not None else None  # Модуль и округление
            student_by_groups["groups"][group_name]["average_grade"] = average_grade_rounded

        return Response(student_by_groups)


class GradeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data: dict[str, Any] = request.data

        semester = data.get("semester")
        discipline_id = data.get("discipline_id")
        student_id = data.get("student_id")
        grade = data.get("grade")

        errors = {"errors": []}
        if not semester:
            errors["errors"].append("'semester' is required field")
        if not discipline_id:
            errors["errors"].append("'semester' id is required field")
        if not student_id:
            errors["errors"].append("'student_id' is required field")
        if not grade:
            errors["errors"].append("'grade' is required field")

        if errors["errors"]:
            return Response(errors, status.HTTP_400_BAD_REQUEST)

        Grade.objects.create(semester=semester, discipline_id=discipline_id, student_id=student_id, grade=grade)

        return Response({"status": "success"})

    def put(self, request: Request):
        data: dict[str, Any] = request.data

        grade_id = data.get("grade_id")
        grade_value = data.get("grade_value")

        errors = {"errors": []}

        if not grade_id:
            errors["errors"].append("'grade_id' id is required field")
        if not grade_value:
            errors["errors"].append("'grade_value' is required field")

        if errors["errors"]:
            return Response(errors, status.HTTP_400_BAD_REQUEST)

        grade = Grade.objects.filter(id=int(grade_id)).first()
        if not grade:
            return Response({"error": "Grade does not exist"}, status.HTTP_400_BAD_REQUEST)

        grade.grade = int(grade_value)
        grade.save()

        return Response({"status": "success"})

    def delete(self, request: Request):
        grade_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        grade_query = Grade.objects

        if grade_id:
            grade_query = grade_query.filter(id=grade_id)
        else:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        grade: Grade = grade_query.first()
        if not grade:
            return Response({"error": "Grade does not exist!"}, status.HTTP_404_NOT_FOUND)

        grade.delete()
        return Response({"status": "success"})


class AvailableRoomsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rooms = Room.objects.values("id", "number").all()
        return Response({"available_rooms": rooms})


class TimeSlotsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        time_slots = TimeSlot.objects.order_by("day_of_week", "start_time").all()

        formatted_time_slots = []
        for time_slot in time_slots:
            formatted_time_slots.append(
                {
                    "id": time_slot.id,
                    "start_time": time_slot.start_time.strftime("%H:%M"),
                    "end_time": time_slot.end_time.strftime("%H:%M"),
                    "day_of_week": time_slot.day_of_week,
                    "day_of_week_display": time_slot.get_day_of_week_display(),
                }
            )

        return Response({"time_slots": formatted_time_slots}, status=status.HTTP_200_OK)

    def post(self, request: Request):
        data: dict[str, Any] = request.data
        start_time = datetime.strptime(data.get("start_time"), "%H:%M") if data.get("start_time") else None
        end_time = datetime.strptime(data.get("end_time"), "%H:%M") if data.get("end_time") else None
        day_of_week = TimeSlot.DayOfWeek(data.get("day_of_week")) if data.get("day_of_week") else None

        errors = {"errors": []}

        if not start_time:
            errors["errors"].append("'start_time' id is required field")
        if not end_time:
            errors["errors"].append("'end_time' is required field")
        if not day_of_week:
            errors["errors"].append("'day_of_week' id is required field")

        if errors["errors"]:
            return Response(errors, status.HTTP_400_BAD_REQUEST)

        TimeSlot.objects.create(start_time=start_time, end_time=end_time, day_of_week=day_of_week)

        return Response({"status": "success"})

    def delete(self, request: Request):
        time_slot_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        time_slot_query = TimeSlot.objects

        if time_slot_id:
            time_slot_query = time_slot_query.filter(id=time_slot_id)
        else:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        time_slot: TimeSlot = time_slot_query.first()
        if not time_slot:
            return Response({"error": "Time Slot does not exist!"}, status.HTTP_404_NOT_FOUND)

        time_slot.delete()
        return Response({"status": "success"})


class DisciplinesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        disciplines = Discipline.objects.values("id", "name").all()
        return Response(disciplines)

    def post(self, request: Request):
        data: dict[str, Any] = request.data
        name = data.get("name")

        if not name:
            return Response({"error": "'name' is required field"}, status.HTTP_400_BAD_REQUEST)

        Discipline.objects.create(name=name)

        return Response({"status": "success"})

    def delete(self, request: Request):
        discipline_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        discipline_query = Discipline.objects

        if discipline_id:
            discipline_query = discipline_query.filter(id=discipline_id)
        else:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        discipline: Discipline = discipline_query.first()
        if not discipline:
            return Response({"error": "Discipline does not exist!"}, status.HTTP_404_NOT_FOUND)

        discipline.delete()
        return Response({"status": "success"})


class ScheduleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        group = request.query_params.get("group")
        semester = request.query_params.get("semester")
        print(f"Received group: {group}, semester: {semester}")

        errors = {"errors": []}

        if not group:
            errors["errors"].append("'group' is required field")
        if not semester:
            errors["errors"].append("'semester' is required field")

        if errors["errors"]:
            return Response(errors, status.HTTP_400_BAD_REQUEST)

        schedules = Schedule.objects.order_by("timeslot__day_of_week", "timeslot__start_time").filter(
            group__name=group, semester=semester
        )

        formatted_schedules = []

        for schedule in schedules:
            formatted_schedules.append(
                {
                    "id": schedule.id,
                    "time_slot": {
                        "id": schedule.timeslot.id,
                        "day_of_week": schedule.timeslot.day_of_week,
                        "day_of_week_display": schedule.timeslot.get_day_of_week_display(),
                        "start_time": schedule.timeslot.start_time.strftime("%H:%M"),
                        "end_time": schedule.timeslot.end_time.strftime("%H:%M"),
                    },
                    "room": {
                        "id": schedule.room.id,
                        "name": schedule.room.number,
                    },
                    "discipline": {
                        "id": schedule.discipline.id,
                        "name": schedule.discipline.name,
                    },
                    "teacher": {
                        "id": schedule.teacher.id,
                        "name": schedule.teacher.name,
                    },
                }
            )

        return Response({"schedule": formatted_schedules})

    def post(self, request: Request):
        data: dict[str, Any] = request.data
        semester = data.get("semester")
        group_name = data.get("group_name")
        time_slot_id = data.get("time_slot_id")
        room_id = data.get("room_id")
        discipline_id = data.get("discipline_id")
        teacher_id = data.get("teacher_id")

        errors = {"errors": []}

        if not semester:
            errors["errors"].append("'semester' is a required field")
        if not group_name:
            errors["errors"].append("'group_name' is a required field")
        if not time_slot_id:
            errors["errors"].append("'time_slot_id' is a required field")
        if not room_id:
            errors["errors"].append("'room_id' is a required field")
        if not discipline_id:
            errors["errors"].append("'discipline_id' is a required field")
        if not teacher_id:
            errors["errors"].append("'teacher_id' is a required field")

        if errors["errors"]:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return Response({"error": f"Group '{group_name}' does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        Schedule.objects.create(
            semester=semester,
            group=group,
            timeslot_id=time_slot_id,
            room_id=room_id,
            discipline_id=discipline_id,
            teacher_id=teacher_id,
        )

        return Response({"status": "success"}, status=status.HTTP_201_CREATED)

    def delete(self, request: Request):
        schedule_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        schedule_query = Schedule.objects

        if schedule_id:
            schedule_query = schedule_query.filter(id=schedule_id)
        else:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        schedule: Schedule = schedule_query.first()
        if not schedule:
            return Response({"error": "Schedule does not exist!"}, status.HTTP_404_NOT_FOUND)

        schedule.delete()
        return Response({"status": "success"})

    def put(self, request: Request):
        schedule_id = int(request.query_params.get("id")) if request.query_params.get("id") else None

        if not schedule_id:
            return Response({"error": "'id' is required field"}, status.HTTP_400_BAD_REQUEST)

        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            return Response({"error": "Schedule does not exist!"}, status.HTTP_404_NOT_FOUND)

        data: Dict[str, Any] = request.data

        time_slot_id = data.get("time_slot_id")
        if time_slot_id is not None:
            schedule.timeslot_id = time_slot_id

        room_id = data.get("room_id")
        if room_id is not None:
            schedule.room_id = room_id

        discipline_id = data.get("discipline_id")
        if discipline_id is not None:
            schedule.discipline_id = discipline_id

        teacher_id = data.get("teacher_id")
        if teacher_id is not None:
            schedule.teacher_id = teacher_id

        schedule.save()

        return Response({"status": "success"}, status=status.HTTP_200_OK)
