#Третья лаба

###Практическая работа 3

Нужно было практическим методом изучить работу запросов Django ORM

Модель базы данных:


```
from django.db import models

class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_day = models.DateTimeField(null=True)

class Own(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)

class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()
```

Нужно было написать запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначить удостоверение и от 1 до 3 автомобилей:

![задание](assets/aaa.PNG)
![задание](assets/bbb.PNG)
![задание](assets/ccc.PNG)

Далее нужно было:
Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

![задание](assets/ddd.PNG)

И последнее задание практической работы:
Вывод даты выдачи самого старшего водительского удостоверения
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
Выведите количество машин для каждого водителя
Подсчитайте количество машин каждой марки
Отсортируйте всех автовладельцев по дате выдачи удостоверения

![задание](assets/eee.PNG)

###Цель работы

Описать базу данных средствами Django ORM. Я взял второй вариант - Библиотека.

###Models

```
from django.db import models
from datetime import datetime


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publishing_year = models.DateField()
    cipher = models.CharField(max_length=10)

    def __str__(self):
        return "{}, {}".format(self.author, self.name)


class Hall(models.Model):
    sequence_number = models.IntegerField()
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return "number: {} {}".format(self.sequence_number, self.name)


class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Reader(models.Model):
    EDUCATIONS = [
        ('0', 'no education'),
        ('1', 'elementary'),
        ('2', 'middle'),
        ('3', 'bachelor'),
        ('4', 'master')
    ]
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    passport = models.CharField(max_length=10)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    education = models.CharField(choices=EDUCATIONS, default='0', max_length=1)
    phd = models.BooleanField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    library_card_number = models.CharField(max_length=10)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.second_name)


class Assignment(models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    date_assigned = models.DateField(default=datetime.now())
    date_returned = models.DateField(default=None, blank=True, null=True)
```

###Urls

```
from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path('books/all', BookListView.as_view()),
    path('books/<int:pk>', BookRetrieveView.as_view()),
    path('books/update/<int:pk>', BookUpdateView.as_view()),
    path('books/new', BookCreateView.as_view()),

    path('halls/all', HallListView.as_view()),
    path('halls/<int:pk>', HallRetrieveView.as_view()),
    path('halls/update/<int:pk>', HallUpdateView.as_view()),
    path('halls/new', HallCreateView.as_view()),

    path('copys/all', CopyListView.as_view()),
    path('copys/<int:pk>', CopyRetrieveView.as_view()),
    path('copys/update/<int:pk>', CopyUpdateView.as_view()),
    path('copys/new', CopyCreateView.as_view()),

    path('readers/all', ReaderListView.as_view()),
    path('readers/<int:pk>', ReaderRetrieveView.as_view()),
    path('readers/update/<int:pk>', ReaderUpdateView.as_view()),
    path('readers/new', ReaderCreateView.as_view()),
    path('readers/assignments/<int:pk>', ReaderRetrieveAssignmentsView.as_view()),
    path('readers/debtors', ReadersRetrieveDebtorView.as_view()),
    path('readers/rareBooks', ReadersRetrieveRareBooksView.as_view()),
    path('readers/young', YoungReadersCountView.as_view()),
    path('readers/education', ReadersEducationCountView.as_view()),

    path('assignments/all', AssignmentListView.as_view()),
    path('assignments/<int:pk>', AssignmentRetrieveView.as_view()),
    path('assignments/update/<int:pk>', AssignmentUpdateView.as_view()),
    path('assignments/new', AssignmentCreateView.as_view()),
]
```

###Serializer

```
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author']

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer()
    hall = HallSerializer()
    class Meta:
        model = Copy
        fields = '__all__'


class CreateCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = '__all__'

class CopyShortSerializer(serializers.ModelSerializer):
    book = BookShortSerializer()
    class Meta:
        model = Copy
        fields = ['book']

class ReaderSerializer(serializers.ModelSerializer):
    hall = HallSerializer()
    education = serializers.CharField(source='get_education_display')

    class Meta:
        model = Reader
        fields = '__all__'


class CreateReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class EducationSerializer(serializers.Serializer):
    education = serializers.CharField()
    education_name = serializers.SerializerMethodField()
    percentage = serializers.SerializerMethodField()

    def get_education_name(self, object):
        return dict(Reader.EDUCATIONS).get(object['education'], object['education'])

    def get_percentage(self, object):
        readers_cnt = Reader.objects.count()
        education_cnt = Reader.objects.filter(education=object['education']).count()
        return (education_cnt / readers_cnt) * 100

    def create(self, validated_data):
        pass


class ReaderShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['name', 'second_name', 'surname']


class AssignmentSerializer(serializers.ModelSerializer):
    copy = CopySerializer()
    reader = ReaderSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentShortSerializer(serializers.ModelSerializer):
    copy = CopyShortSerializer()

    class Meta:
        model = Assignment
        fields = ['copy']


class AssignmentDebtorSerializer(serializers.ModelSerializer):
    reader = ReaderShortSerializer()

    class Meta:
        model = Assignment
        fields = ['reader']


class CreateAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
```


###Views

```
import datetime
from datetime import timedelta
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from django.db.models import Q
from django.db.models import Count, Subquery
from rest_framework.views import APIView

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HallListView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallRetrieveView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallUpdateView(generics.UpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallCreateView(generics.CreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class CopyListView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyRetrieveView(generics.RetrieveAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyUpdateView(generics.UpdateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CreateCopySerializer


class CopyCreateView(generics.CreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CreateCopySerializer


class ReaderListView(generics.ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderRetrieveView(generics.RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderUpdateView(generics.UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = CreateReaderSerializer


class ReaderCreateView(generics.CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = CreateReaderSerializer

class ReaderRetrieveAssignmentsView(generics.ListAPIView):
    serializer_class = AssignmentShortSerializer

    def get_queryset(self):
        reader_id = self.kwargs['pk']
        assignment = Assignment.objects.filter(Q(reader__pk=reader_id) & Q(date_returned__isnull=True))
        return assignment


class ReadersRetrieveDebtorView(generics.ListAPIView):
    serializer_class = AssignmentDebtorSerializer

    def get_queryset(self):
        time = datetime.now()
        time -= timedelta(days=30)
        assignments = Assignment.objects.filter(date_assigned__lt=time)
        return assignments


class ReadersRetrieveRareBooksView(generics.ListAPIView):
    serializer_class = ReaderShortSerializer

    def get_queryset(self):
        books = Copy.objects.values('book').annotate(num=Count('id')).filter(num__lte=2)
        readers = Reader.objects.filter(Q(assignment__copy__book__in=Subquery(books.values('book_id'))) & Q(assignment__date_returned__isnull=True)).distinct()

        return readers


class YoungReadersCountView(APIView):
    def get(self, request):
        time = datetime.now() - timedelta(days=365.25 * 20)
        readers = Reader.objects.filter(birth_date__gt=time).count()

        response = {'Readers under 20': readers}
        return Response(response)


class ReadersEducationCountView(APIView):
    def get(self, request):
        education = [{'education': cur[0]} for cur in Reader.EDUCATIONS]
        serializer = EducationSerializer(data=education, many=True)

        if serializer.is_valid():
            response = {'Education percentage': serializer.data}
            return Response(response)
        else:
            return Response(serializer.errors, status=400)

class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentRetrieveView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentUpdateView(generics.UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = CreateAssignmentSerializer


class AssignmentCreateView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = CreateAssignmentSerializer
```

###Работа сайта
####Assignment
get_assignment(index):
![задание](assets/api/get_ass.PNG)

get_asseignments(all):
![задание](assets/api/get_assents1.PNG)
![задание](assets/api/get_assents2.PNG)

put_assignment:
![задание](assets/api/put_ass.PNG)

update_assignment:
![задание](assets/api/update_ass.PNG)

####Book
get_book(index):
![задание](assets/api/get_book.PNG)

get_books(all):
![задание](assets/api/get_books.PNG)

put_book:
![задание](assets/api/put_book.PNG)

update_book:
![задание](assets/api/update_book.PNG)

####Copy
get_copy(index):
![задание](assets/api/get_copy.PNG)

get_copys(all):
![задание](assets/api/get_copys.PNG)

put_copy:
![задание](assets/api/put_copy.PNG)

update_copy:
![задание](assets/api/update_copy.PNG)

####Hall
get_hall(index):
![задание](assets/api/get_hall.PNG)

get_halls(all):
![задание](assets/api/get_halls.PNG)

put_hall:
![задание](assets/api/put_hall.PNG)

update_hall:
![задание](assets/api/update_hall1.PNG)

####Reader
get_reader(index):
![задание](assets/api/get_reader.PNG)

get_readers(all):
![задание](assets/api/get_readers.PNG)

put_reader:
![задание](assets/api/put_reader.PNG)

update_reader:
![задание](assets/api/update_reader.PNG)