from django.db import models

class Warrior(models.Model):
    race_types = {
        "a": "student",
        "d": "developer",
        "t":"teamlead"
    }

    race = models.CharField(max_length=1, choices=race_types, verbose_name="Pacca")
    name = models.CharField(max_length=120, verbose_name="Имя")
    level = models.IntegerField(verbose_name="Уровень", default=1)
    skill = models.ManyToManyField("Skill", verbose_name="Умения", through="SkillOfWarrior",
                                   related_name="warrior_skills")
    profession = models.ForeignKey("Profession", on_delete=models.CASCADE, verbose_name="Профессия",
                                   blank=True, null=True)

class Profession(models.Model):

    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

class Skill(models.Model):
    title = models.CharField(max_length=120, verbose_name="Наименование")


class SkillOfWarrior(models.Model):
    """
        Ассоциативная сущность для связи Воин-Скилл
    """
    skill = models.ForeignKey("Skill", verbose_name="Умение", on_delete=models.CASCADE)
    warrior = models.ForeignKey("Warrior", verbose_name="Воин", on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name="Уровень навыка")

