# Лабораторная работа 3

## Цель лабораторной работы
Овладеть практическими навыками и умениями реализации web-сервисов
средствами Django.

## Практическое задание
Реализовать сайт, используя фреймворк Django 3, Django REST Framework, Djoser и
СУБД PostgreSQL *, в соответствии с вариантом задания лабораторной работы.

## Описание работы (вариант 2)
Создать программную систему, предназначенную для работников библиотеки. Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке книгах, о читателях библиотеки и читальных залах.

Для каждой книги в БД должны храниться следующие сведения: название книги, автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале библиотеки, а также шифр книги и дата закрепления книги за читателем. Книги могут перерегистрироваться в другом зале.

Сведения о читателях библиотеки должны включать номер читательского билета, ФИО читателя, номер паспорта, дату рождения, адрес, номер телефона, образование, наличие ученой степени.

Читатели закрепляются за определенным залом, могут переписаться в другой зал и могут записываться и выписываться из библиотеки.

Библиотека имеет несколько читальных залов, которые характеризуются номером, названием и вместимостью, то есть количеством людей, которые могут одновременно работать в зале.

Библиотека может получать новые книги и списывать старые. Шифр книги может измениться в результате переклассификации, а номер читательского билета в результате перерегистрации.

## Реализация функционала
- Записать в библиотеку нового читателя.
- Исключить из списка читателей людей, записавшихся в библиотеку более года
назад и не прошедших перерегистрацию.
- Списать старую или потерянную книгу.
- Принять книгу в фонд библиотеки.

#### models.py
    class User(AbstractUser):
        REQUIRED_FIELDS = ['first_name', 'last_name']
    
        def __str__(self):
            return self.username
    
    
    class BookInstance(models.Model):
        section = models.CharField(max_length=20, verbose_name='Секция')
        code = models.CharField(max_length=20, verbose_name='Артикул экземпляра')
        year = models.IntegerField(verbose_name='Год издания')
        conditions = (
            ('a', 'высокое'),
            ('b', 'среднее'),
            ('с', 'низкое'),
        )
        condition = models.CharField(max_length=1, choices=conditions, verbose_name='Состояние экземпляра')
        book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE,related_name='book_instances' )
        reader = models.ForeignKey('Reader', on_delete=models.SET_NULL, null=True,
                                   related_name='book_instances', verbose_name='Читатель', blank=True)
        room = models.ForeignKey('Room', related_name='book_instances', verbose_name='Зал',
                                 on_delete=CASCADE, null=True, blank=True)
        date_issue = models.DateTimeField(verbose_name='Последняя дата выдачи', blank=True, null=True)
    
        def __str__(self):
            return self.code
    
    
    class Book(models.Model):
        name = models.CharField(max_length=50, verbose_name='Название')
        author = models.CharField(max_length=70, verbose_name="Автор(ы)")
        publisher = models.CharField(max_length=30, verbose_name='Издательство')
    
        def __str__(self):
            return self.name
    
    
    class Reader(models.Model):
        ticket = models.CharField(max_length=20, verbose_name='Номер билета читателя')
        name = models.CharField(max_length=70, verbose_name="ФИО")
        passport = models.CharField(max_length=20, verbose_name='Номер паспорта')
        birth_date = models.DateField(verbose_name='Дата рождения')
        address = models.CharField(max_length=100, verbose_name='Адрес')
        phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
        educations = (
            ('н', 'начальное'),
            ('с', 'среднее'),
            ('в', 'высшее'),
        )
        education = models.CharField(max_length=1, choices=educations, verbose_name='Образование')
        degree = models.BooleanField(default=False, verbose_name='Наличие ученой степени')
        registration_date = models.DateField(verbose_name='Дата регистрации')
        room = models.ForeignKey('Room', related_name='readers', verbose_name='Зал, за которым закреплен читатель',
                                 on_delete=CASCADE, null=True)
    
        def __str__(self):
            return self.name
    
    
    
    class Room(models.Model):
        name = models.CharField(max_length=20, verbose_name='Название')
        capacity = models.IntegerField(verbose_name='Вместимость')
    
        def __str__(self):
            return self.name

#### views.py

    from django.db.models.query import QuerySet
    from django.shortcuts import render
    from rest_framework.response import Response
    from rest_framework.views import APIView
    
    from .models import *
    from .serializers import *
    from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
    from rest_framework.permissions import IsAuthenticated
    
    
    # просмотр информации о читателях
    class ReaderListAPIView(ListAPIView):
        serializer_class = ReaderSerializer
        queryset = Reader.objects.all()
    
    
    # создание читателя
    class CreateReaderAPIView(CreateAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = ReaderSerializer
        queryset = Reader.objects.all()
    
    
    # просмотр всех произведений в библиотеке
    class BookListAPIView(ListAPIView):
        serializer_class = BookSerializer
        queryset = Book.objects.all()
    
    
    # появление нового произведения в библиотеке
    class CreateBookAPIView(CreateAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = BookSerializer
        queryset = Book.objects.all()
    
    
    # просмотр экземпляров произведений
    class BookInstanceAPIView(ListAPIView):
        serializer_class = BookInstanceSerializer
        queryset = BookInstance.objects.all()
    
    # появление нового экземпляра произведения в библиотеке
    class CreateInstanceAPIView(CreateAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = BookInstanceSerializer
        queryset = BookInstance.objects.all()
    
    
    # редактирование и удаление произведений
    class OneBookAPIView(RetrieveUpdateDestroyAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = BookSerializer
        queryset = Book.objects.all()
    
    
    # редактирование и удаление экземпляров
    class OneInstanceAPIView(RetrieveUpdateDestroyAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = BookInstanceSerializer
        queryset = BookInstance.objects.all()
    
    
    # редактирование и удаление читателей
    class ReaderDetailAPIView(RetrieveUpdateDestroyAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = ReaderSerializer
        queryset = Reader.objects.all()
    
    #просмотр всех читательских залов библиотеки
    class RoomListAPIView(ListAPIView):
        serializer_class = RoomSerializer
        queryset = Room.objects.all()

    # отправка, просмотр, удаление всех взятых книг
    class BookTakingListAPIView(ListAPIView):
        serializer_class = BookTakingSerializer
        queryset = BookTaking.objects.all()
    
    
    class BookTakingPostAPIView(CreateAPIView):
        serializer_class = BookTakingSerializer
        queryset = BookTaking.objects.all()
    
    
    class BookTakingDeleteApiView(RetrieveUpdateDestroyAPIView):
        serializer_class = BookTakingSerializer
        queryset = BookTaking.objects.all()

### swagger

    schema_view = get_schema_view(
        openapi.Info(
            title="API",
            default_version='v2',
            description="Description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="kostyalol15@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
    )

![image info](swagger.png)

## Возникшие трудности
Самым сложным оказалось настройка токенов, поскольку документация имеет устаревший вид, из-за этого приходилось 
заходить в src файлы и смотреть, как работает код. 
Как оказалось переменная `DEFAULT_AUTHENTICATION_CLASSES` 
должна быть не классом, а массивом, поскольку в текущей версии django, функция настройки просто итерируется по этому конфигу 
и создает инстансы класса.

Следующей проблемой было придумать вообще то, как будут взаимодействовать данные, в какой форме их выдавать.
Если посудить за ходом рассуждений, то можно понять, что у нас есть сущность книга - ну просто набор букв и слов от автора, которые потом распечатывают издания. 
Ага, издания, значит у книг может быть множество копий и все они могут быть напечатаны в разное время. Значит следует добавить еще одну сущность, которая будет содержать в себе все детали.
При этом у них еще может быть и разное качество, 
как например в школе у нас было три состояния: 
идеальное, хорошее, удовлетворительное. 
Введем эти поля и получается, 
что book instance будет содержать в себе внешний ключ на книгу.

Далее разбираемся с читателем - кто это вообще, как его идентифицировать. С Мариной Михайловной я делал ЛР по ресторанам, 
там мы вводили сущность человека, у которого есть номер телефона и паспортные данные. таким образом мы сразу достигаем уникальности пользователя, поскольку 
у двух людей не может быть одинакового номера паспорта. Далее учитываем все поля необходимые в лр и получаем готовую сущность

Далее надо разобраться с тем, как вообще происходит взятие. Если смотреть на жизнь, то видно, что приходит читатель, работник записывает на него экземпляр и выдает ему на руки. 
Тут система та же, у нас есть сущность BookTaking, которая говорит, что вот такой-то читатель взял такой-то экземпляр

