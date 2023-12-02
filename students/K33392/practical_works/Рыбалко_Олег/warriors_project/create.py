from warriors_app.models import *

# Create Skills
skill1 = Skill.objects.create(title="Sword Fighting")
skill2 = Skill.objects.create(title="Archery")
skill3 = Skill.objects.create(title="Magic Spells")

# Create Professions
profession1 = Profession.objects.create(
  title="Knight", description="Master of sword fighting"
)
profession2 = Profession.objects.create(title="Archer", description="Expert in archery")
profession3 = Profession.objects.create(
  title="Wizard", description="Skilled in magic spells"
)

# Create Warriors with Skills and Professions
warrior1 = Warrior.objects.create(
  race="s", name="Student Warrior", level=5, profession=profession1
)
warrior2 = Warrior.objects.create(
  race="d", name="Developer Warrior", level=8, profession=profession2
)
warrior3 = Warrior.objects.create(
  race="t", name="Teamlead Warrior", level=10, profession=profession3
)

# Assign Skills to Warriors
skill_of_warrior1 = SkillOfWarrior.objects.create(
  skill=skill1, warrior=warrior1, level=3
)
skill_of_warrior2 = SkillOfWarrior.objects.create(
  skill=skill2, warrior=warrior2, level=5
)
skill_of_warrior3 = SkillOfWarrior.objects.create(
  skill=skill3, warrior=warrior3, level=7
)
