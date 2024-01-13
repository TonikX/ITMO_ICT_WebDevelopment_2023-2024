#Описание моделей
___
<br>

##*Lesson (Занятия)*
<br>

Модель ***Lesson*** представляет занятие и содержит следующие поля: <br>
- **name (название):** CharField с максимальной длиной 100 символов

<br><br>

##*Teacher (Учителя)*
<br>

Модель ***Teacher*** представляет учителя и содержит следующие поля: <br>
- **name (имя):** CharField с максимальной длиной 100 символов

<br><br>

##*LessonTeacher (Урок-Учитель)*
<br>

Модель ***LessonTeacher*** представляет занятие и содержит следующие поля: <br>
- **Lesson (название):** ForeignKey с ссылкой на модель *Lesson* <br>
- **Teacher (учитель):** ForeignKey с ссылкой на модель *Teacher* <br>
<br><br>

##*StudentClass (Класс)*
<br>

Модель ***StudentClass*** представляет учебный класс и содержит следующие поля: <br>
- **letter (буква):** CharField с максимальной длиной 2 символа <br>
- **year (год):** IntegerField

<br><br>

##*Student (обучающийся)*
<br>

Модель ***Student*** представляет обучающегося и содержит следующие поля: <br>
- **name (имя):** CharField с максимальной длиной 100 символов <br>
- **age (возраст):** PositiveIntegerField <br>
- **sex (пол):** CharField с максимальной длиной 2 символа <br>
- **student_class (класс):** ForeignKey с ссылкой на модель *StudentClass* <br>
<br><br>

##*Room (аудитория)*
<br>

Модель ***Room*** представляет аудиторию и содержит следующие поля: <br>
- **num (номер):** CharField с максимальной длиной 4 символа <br>
- **base :** BooleanField

<br><br>

##*Schedule (расписание)*
<br>

Модель ***Schedule*** представляет аудиторию и содержит следующие поля: <br>
- **day (день):** CharField с максимальной длиной 10 символов <br>
- **base :** BooleanField <br>
- **num_lesson (номер урока):** IntegerField <br>
- **student_class (класс):** ForeignKey с ссылкой на модель *StudentClass* <br>
- **room (аудитория):** ForeignKey с ссылкой на модель *Room* <br>
- **lesson_teacher (класс):** ForeignKey с ссылкой на модель *LessonTeacher* <br>
<br><br>

##*Mark (оценка)*
<br>

Модель ***Mark*** представляет оценку и содержит следующие поля: <br>
- **student (обучающийся):** ForeignKey с ссылкой на модель *Student* <br>
- **schedule (расписание):** ForeignKey с ссылкой на модель *Schedule* <br>
- **mark (оценка):** IntegerField <br>

<br><br>

#Сериалайзеры
___
<br/>

##*RoomSerializer*
<br/>

Класс **RoomSerializer** является сериалайзером для модели **Room**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **num (номер)** <br>
- **base** 
<br><br>

##*TeacherSerializer*
<br/>

Класс **TeacherSerializer** является сериалайзером для модели **Teacher**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **name (имя)** CharField
<br><br>

##*LessonSerializer*
<br/>

Класс **LessonSerializer** является сериалайзером для модели **Lesson**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **name (название)**
<br><br>




##*CountTeachersSerializer*
<br/>

Класс **CountTeachersSerializer** является сериалайзером для модели **Lesson**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id**
- **name**
- **count**
<br><br>


##*ShowOtherTeachersSerializers*
<br/>

Класс **ShowOtherTeachersSerializers** является сериалайзером для модели **Lesson**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id**
- **name**
- **teachers**
<br><br>

##*LessonTeacherSerializer*
<br/>

Класс **LessonTeacherSerializer** является сериалайзером для модели **LessonTeacher**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **Lesson (название)** <br>
- **Teacher (название)** <br>
<br><br>

##*ShowLessonTeacherSerializer*
<br/>

Класс **ShowLessonTeacherSerializer** является сериалайзером для модели **LessonTeacher**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id** <br/>
- **Lesson (название)** <br>
- **Teacher (имя)** <br>
<br><br>

##*MarkSerializer*
<br/>

Класс **MarkSerializer** является сериалайзером для модели **Mark**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **student (обучающийся)** <br>
- **schedule (расписание)** <br>
- **mark (оценка)** <br>
<br><br>

##*ShowMarkSerializer*
<br/>

Класс **ShowMarkSerializer** является сериалайзером для модели **Mark**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id** <br/>
- **student (обучающийся)** <br>
- **schedule (расписание)** <br>
- **mark (оценка)** <br>
<br><br>

##*StudentSerializer*
<br/>

Класс **StudentSerializer** является сериалайзером для модели **Student**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **name (имя)** <br>
- **age (возраст)** <br>
- **sex (пол)** <br>
- **student_class (класс)** <br>
<br><br>

##*ShowStatlessonSerializer*
<br/>

Класс **ShowStatlessonSerializer** является сериалайзером для модели **Lesson**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id** <br/>
- **name (название)** <br>
- **students (обучающиеся)** <br>
<br><br>

##*StudentSerializer*
<br/>

Класс **StudentClassSerializer** является сериалайзером для модели **StudentClass**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **letter (буква)** <br>
- **year (год)**
<br><br>

##*CountBGClassSerializer*
<br/>

Класс **CountBGClassSerializer** является сериалайзером для модели **StudentClass**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id** <br/>
- **letter (буква)** <br>
- **year (год)**
- **boys**
- **girls**
<br><br>

##*ScheduleSerializer*
<br/>

Класс **ScheduleSerializer** является сериалайзером для модели **Schedule**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **day (день)** <br>
- **base** <br>
- **num_lesson (номер урока)** <br>
- **student_class (класс)** <br>
- **room (аудитория)** <br>
- **lesson_teacher (класс)** <br>
<br><br>

##*FindScheduleSerializer*
<br/>

Класс **FindScheduleSerializer** является сериалайзером для модели **Schedule**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id** <br/>
- **day (день)** <br>
- **num_lesson (номер урока)** <br>
- **room (аудитория)** <br>
<br><br>

##*ShowScheduleSerializer*
<br/>

Класс **FindScheduleSerializer** является сериалайзером для модели **ShowScheduleSerializer**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **id** <br/>
- **day (день)** <br>
- **num_lesson (номер урока):** <br>
- **room (аудитория)** <br>
- **student_class (класс)** <br>
- **lesson (название)** <br>
- **teacher (имя)** <br>
<br><br>

##*RegistrationSerializer*
<br/>

Класс **RegistrationSerializer** является сериалайзером для модели **User**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **username** <br/>
- **type** <br>
- **password** <br>
- **password2** <br>
<br><br>

##*LoginSerializer*
<br/>

Класс **LoginSerializer** является сериалайзером для модели **User**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **username** <br/>
- **password** <br>
<br><br>

##*LoginSerializer*
<br/>

Класс **LoginSerializer** является сериалайзером для модели **User**. <br/>
Он наследует от **serializers.ModelSerializer**
<br><br>

##*PasswordChangeSerializer*
<br/>

Класс **PasswordChangeSerializer** является сериалайзером для модели **User**. <br/>
Он наследует от **serializers.ModelSerializer** и определяет следующие поля: <br/>
- **current_password** <br/>
- **new_password** <br>
<br><br>


#Роутер
___
<br/>

##school/urls.ry
<br/>

```python
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('app.urls')),
]
```

<br/>

##app/urls.ry
<br/>

```python
from rest_framework import routers
from django.urls import path, include
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

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),

    path('', include(router.urls)),
]

```
<br/>

#Эндпоинты
___
<br/>

##*Регистрация*
<br/>

-**Эндпойнт:** /main/register/ <br/>
-**Метод:** POST <br/>
-**Описание:** Регистрация пользователя<br/>
<br/>

##*Логин*
<br/>

-**Эндпойнт:** /main/login/ <br/>
-**Метод:** POST <br/>
-**Описание:** Вход в систему<br/>
<br/>

##*Логаут*
<br/>

-**Эндпойнт:** /main/logout/ <br/>
-**Метод:** POST <br/>
-**Описание:** Выход из системы<br/>
<br/>

##*Аудитории*
<br/>

-**Эндпойнт:** /main/rooms/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить все аудитории <br/>
<br/>

##*Обычные аудитории*
<br/>

-**Эндпойнт:** /main/rooms/count-base/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить все обычные аудитории <br/>
<br/>

##*Специализированные аудитории*
<br/>

-**Эндпойнт:** /main/rooms/count_specific/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить все специализированные аудитории <br/>
<br/>

##*Учителя*
<br/>

-**Эндпойнт:** /main/teachers/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить всех учителей <br/>
<br/>


##*Занятия*
<br/>

-**Эндпойнт:** /main/lessons/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить все занятия <br/>
<br/>

##*Подсчет учителей урока*
<br/>

-**Эндпойнт:** /main/lessons/how_many_teachers/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить количество учителей ведущих предмет <br/>
<br/>

##*Учитель-занятие*
<br/>

-**Эндпойнт:** /main/teachers-lessons/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить все пары учитель-занятие <br/>
<br/>

##*Обучающиеся*
<br/>

-**Эндпойнт:** /main/students/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить всех обучающихся <br/>
<br/>

##*Классы*
<br/>

-**Эндпойнт:** /main/classes/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить все классы <br/>
<br/>

##*Количество мальчиков и девочек в классе*
<br/>

-**Эндпойнт:** /main/classes/\*/count_boys_and_girls/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить мальчиков и девочек в классе \* <br/>
<br/>

##*Все обучающихся в классе*
<br/>

-**Эндпойнт:** /classes/\*/show_students/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить всех обучающихся в классе \* <br/>
<br/>

##*Успеваемость класса*
<br/>

-**Эндпойнт:** /main/classes/\*/statistics/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить успеваемость класса \* <br/>
<br/>

##*Расписание*
<br/>

-**Эндпойнт:** /main/schedules/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить расписание<br/>
<br/>

##*Поиск по расписанию*
<br/>

-**Эндпойнт:** /main/schedules/find/ <br/>
-**Метод:** POST <br/>
-**Описание:** Поиск по расписанию<br/>
<br/>

##*Оценки*
<br/>

-**Эндпойнт:** /main/marks/ <br/>
-**Метод:** GET <br/>
-**Описание:** Получить оценки<br/>
<br/>





























