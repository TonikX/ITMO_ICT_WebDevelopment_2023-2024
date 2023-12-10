from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username


class BookTaking(models.Model):
    book_instance = models.ForeignKey(
        'BookInstance',
        verbose_name='Экземпляр книги',
        on_delete=CASCADE,
        related_name='book_taking'
    )

    reader = models.ForeignKey('Reader', on_delete=models.CASCADE,
                               related_name='book_taking', verbose_name='Читатель')
    data_issue = models.DateField(verbose_name='Последняя дата выдачи', blank=True, null=True)
    #data_issue = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book_instance} {self.reader}'


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
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE, related_name='book_instances')

    room = models.ForeignKey('Room', related_name='book_instances', verbose_name='Зал',
                             on_delete=CASCADE, null=True, blank=True)

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
