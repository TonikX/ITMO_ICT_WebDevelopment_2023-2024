import { createRouter, createWebHistory } from "vue-router";
import Login from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";
import AddRoom from "@/components/Room/AddRoom.vue";
import RoomList from "@/components/Room/RoomList.vue";
import RoomPage from "@/components/Room/RoomPage.vue";
import AddTeacher from "@/components/Teacher/AddTeacher.vue";
import TeacherList from "@/components/Teacher/TeacherList.vue";
import TeacherPage from "@/components/Teacher/TeacherPage.vue";
import AddTeacherLesson from "@/components/TeacherLesson/AddTeacherLesson.vue";
import TeacherLessonList from "@/components/TeacherLesson/TeacherLessonList.vue";
import TeacherLessonPage from "@/components/TeacherLesson/TeacherLessonPage.vue";
import AddLesson from "@/components/Lesson/AddLesson.vue";
import LessonList from "@/components/Lesson/LessonList.vue";
import LessonPage from "@/components/Lesson/LessonPage.vue";
import AddClass from "@/components/Class/AddClass.vue";
import ClassList from "@/components/Class/ClassList.vue";
import ClassPage from "@/components/Class/ClassPage.vue";
import ClassStudentsPage from "@/components/Class/ClassStudentsPage.vue";
import StudentPage from "@/components/Students/StudentPage.vue";
import AddStudent from "@/components/Students/AddStudent.vue";
import ScheduleList from "@/components/Schedule/ScheduleList.vue";
import AddSchedule from "@/components/Schedule/AddSchedule.vue";
import SchedulePage from "@/components/Schedule/SchedulePage.vue";
import CountTeachersPage from "@/components/Lesson/CountTeachersPage.vue";
import FindConcrete from "@/components/Schedule/FindConcrete.vue";
import AddMark from "@/components/Mark/AddMark.vue";
import ShowStatistics from "@/components/Class/ShowStatistics.vue";
import MarkList from "@/components/Mark/MarkList.vue";
import MarkPage from "@/components/Mark/MarkPage.vue";

const routes = [
  { path: "/login", component: Login },
  { path: "/register", component: RegisterPage },
  { path: "/add-room", component: AddRoom },
  { path: "/rooms", component: RoomList },
  { path: "/rooms/:id", component: RoomPage },
  { path: "/add-teacher", component: AddTeacher },
  { path: "/teachers", component: TeacherList },
  { path: "/teachers/:id", component: TeacherPage },
  { path: "/add-teacher-lesson", component: AddTeacherLesson },
  { path: "/teachers-lessons", component: TeacherLessonList },
  { path: "/teachers-lessons/:id", component: TeacherLessonPage },
  { path: "/add-lesson", component: AddLesson },
  { path: "/lessons", component: LessonList },
  { path: "/count-teachers", component: CountTeachersPage },
  { path: "/lessons/:id", component: LessonPage },
  { path: "/add-class", component: AddClass },
  { path: "/classes", component: ClassList },
  { path: "/classes/:id", component: ClassPage },
  { path: "/classes/:id/students", component: ClassStudentsPage },
  { path: "/add-student", component: AddStudent },
  { path: "/students/:id", component: StudentPage },
  { path: "/add-schedule", component: AddSchedule },
  { path: "/schedules/:id", component: SchedulePage },
  { path: "/schedules/:id/add-mark", component: AddMark },
  { path: "/schedules/", component: ScheduleList },
  { path: "/find-concrete", component: FindConcrete },
  { path: "/classes/:id/statistics", component: ShowStatistics },
  { path: "/marks/:id", component: MarkPage },
  { path: "/marks", component: MarkList },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
