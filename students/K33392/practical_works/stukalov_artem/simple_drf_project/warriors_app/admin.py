from django.contrib import admin
from . import models

admin.site.register(models.Warrior)
admin.site.register(models.Skill)
admin.site.register(models.Profession)
admin.site.register(models.SkillOfWarrior)
