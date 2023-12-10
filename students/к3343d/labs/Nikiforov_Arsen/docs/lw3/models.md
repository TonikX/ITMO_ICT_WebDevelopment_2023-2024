# models.py

Этот код использует фреймворк Django для создания моделей данных. 
Он определяет структуру базы данных для хранения информации о воинах, их профессиях и умениях.

## Warrior (Воин):

- Содержит информацию о воинах, такую как их имя, уровень, расса (студент, разработчик, руководитель), профессия и умения.
- Использует поле CharField для рассы, CharField для имени, IntegerField для уровня.
- Связан с профессиями и умениями через внешние ключи и многие ко многим отношения.

## Profession (Профессия):

- Содержит информацию о профессиях воинов, такую как название и описание.
- Использует CharField для названия и TextField для описания.

## Skill (Умение):

- Описывает умения, которыми владеют воины.
- Использует CharField для наименования умения.

## SkillOfWarrior (Умение война):

- Связывает воинов с их умениями и указывает уровень освоения умения.
- Использует внешние ключи для связи с воинами и умениями, а также IntegerField для уровня.

Эти модели представляют схему БД для моего проекта, где воины имеют профессии и умения.



```
from django.db import models

class Warrior(models.Model):
   """
   Описание война
   """

   race_types = (
       ('s', 'student'),
       ('d', 'developer'),
       ('t', 'teamlead'),
   )
   race = models.CharField(max_length=1, choices=race_types, verbose_name='раса')
   name = models.CharField(max_length=120, verbose_name='Имя')
   level = models.IntegerField(verbose_name='Уровень', default=0)
   skills = models.ManyToManyField('Skill', verbose_name='Умения', through='SkillOfWarrior',
                                  related_name='warrior_skils')
   profession = models.ForeignKey('Profession', on_delete=models.CASCADE, verbose_name='Профессия',
                                  blank=True, null=True)


class Profession(models.Model):
   """
   Описание профессии
   """

   title = models.CharField(max_length=120, verbose_name='Название')
   description = models.TextField(verbose_name='Описание')


class Skill(models.Model):
   """
   Описание умений
   """

   title = models.CharField(max_length=120, verbose_name='Наименование')

   def __str__(self):
       return self.title


class SkillOfWarrior(models.Model):
   """
   Описание умений война
   """

   skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE)
   warrior = models.ForeignKey('Warrior', verbose_name='Воин', on_delete=models.CASCADE)
   level = models.IntegerField(verbose_name='Уровень освоения умения')
```