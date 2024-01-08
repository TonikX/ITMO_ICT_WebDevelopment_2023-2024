from django.contrib import admin

from warriors_app.models import Warrior, Profession, Skill, SkillOfWarrior

# Register your models here.
admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)
