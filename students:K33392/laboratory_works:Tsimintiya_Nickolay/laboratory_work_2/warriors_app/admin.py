from django.contrib import admin
from models import Warrior, Skill, SkillOfWarrior, Profession
# Register your models here.
admin.site.register(Warrior)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)
admin.site.register(Profession)
