from django.contrib import admin
from .models import Warrior, Profession, Skill, SkillOfWarrior


@admin.register(Warrior)
class WarriorAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'level', 'get_skills', 'profession')
    list_filter = ('race', 'profession')
    search_fields = ('name',)

    def get_skills(self, obj):
        # Получение списка умений в виде строки
        return ", ".join([skill.title for skill in obj.skill.all()])

    get_skills.short_description = 'Умения'


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SkillOfWarrior)
class SkillOfWarriorAdmin(admin.ModelAdmin):
    list_display = ('warrior', 'skill', 'level')
    list_filter = ('warrior__race', 'warrior__profession')
    search_fields = ('warrior__name', 'skill__title')
