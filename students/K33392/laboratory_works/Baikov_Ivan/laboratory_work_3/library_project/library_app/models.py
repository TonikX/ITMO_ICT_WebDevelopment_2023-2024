from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    date_of_creation = models.DateTimeField()
    type = models.CharField(max_length=120, verbose_name='Раздел')
    author = models.CharField(max_length=120, verbose_name='Автор', blank=True, null=True)
    publisher = models.CharField(max_length=120, verbose_name='Издатель', blank=True, null=True)
    halls = models.ManyToManyField('Hall', verbose_name='Залы', through='Availability', related_name='book_halls')
    readers = models.ManyToManyField('Reader', verbose_name='Читатели', through='Ownership', related_name='book_readers')


class Hall(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')
    books = models.ManyToManyField('Book', verbose_name='Книги', through='Availability', related_name='hall_books')


class Reader(models.Model):
    hall = models.ForeignKey('Hall', verbose_name='Зал', on_delete=models.CASCADE, blank=True, null=True)
    FIO = models.CharField(max_length=120, verbose_name='ФИО')
    passport = models.IntegerField(verbose_name='Паспорт')
    phone = models.IntegerField(verbose_name='Телефон')
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=120, verbose_name='Адрес')
    education = models.CharField(max_length=120, verbose_name='Образование')
    qualification = models.CharField(max_length=120, verbose_name='Учёная степень')
    books = models.ManyToManyField('Book', verbose_name='Книги', through='Ownership', related_name='reader_books')


class Availability(models.Model):
   book = models.ForeignKey('Book', verbose_name='Книга', on_delete=models.CASCADE)
   hall = models.ForeignKey('Hall', verbose_name='Зал', on_delete=models.CASCADE)
   amount = models.IntegerField(verbose_name='Количество книг')

   class Meta:
       unique_together = ('book', 'hall')


class Ownership(models.Model):
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=models.CASCADE)
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=models.CASCADE)
    date_of_start = models.DateTimeField()
    date_of_end = models.DateTimeField()

    class Meta:
        unique_together = ('book', 'reader')
