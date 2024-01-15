from django.db import models

class Warrior(models.Model):
    RACE_CHOICES = [
        ('s', 'Short'),
        ('m', 'Medium'),
        ('t', 'Tall'),
    ]
    race = models.CharField(max_length=1, choices=RACE_CHOICES)
    name = models.CharField(max_length=100)
    level = models.IntegerField()

class Skill(models.Model):
    title = models.CharField(max_length=100)

class SkillOfWarrior(models.Model):
   """
   Описание умений война
   """

   skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE)
   warrior = models.ForeignKey('Warrior', verbose_name='Воин', related_name="warrior_skill", on_delete=models.CASCADE)
   level = models.IntegerField(verbose_name='Уровень освоения умения', blank=True, null=True)
