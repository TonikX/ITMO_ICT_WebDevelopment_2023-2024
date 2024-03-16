from warriors_app.models import Warrior, Skill, Profession, SkillOfWarrior

# Создаем скилл (умение)
skill = Skill.objects.create(title="Мастер меча")

# Создаем профессию
profession = Profession.objects.create(title="Воин", description="Мастер боевых искусств")

# Создаем двух воинов
warrior1 = Warrior.objects.create(race='d', name='Алекс', level=5, profession=profession)
warrior2 = Warrior.objects.create(race='s', name='Мария', level=3, profession=profession)

# Связываем воинов с умением
SkillOfWarrior.objects.create(skill=skill, warrior=warrior1, level=2)
SkillOfWarrior.objects.create(skill=skill, warrior=warrior2, level=1)

