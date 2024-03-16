from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register('rooms', viewset=views.RoomViewSet)

router.register('teachers', viewset=views.TeacherViewSet)
router.register('lessons', viewset=views.LessonViewSet)
router.register('teachers-lessons', viewset=views.LessonTeacherViewSet)

router.register('students', viewset=views.StudentViewSet)
router.register('classes', viewset=views.StudentClassViewSet)

router.register('schedules', viewset=views.ScheduleViewSet)
router.register('marks', viewset=views.MarkViewSet)


urlpatterns = router.urls
