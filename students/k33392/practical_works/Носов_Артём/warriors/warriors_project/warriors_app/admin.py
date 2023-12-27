from django.contrib import admin

# Register your models here.
from warriors_app.models import *
admin.site.register(Warrior)
admin.site.register(SkillOfWarrior)
admin.site.register(Profession)
admin.site.register(Skill)