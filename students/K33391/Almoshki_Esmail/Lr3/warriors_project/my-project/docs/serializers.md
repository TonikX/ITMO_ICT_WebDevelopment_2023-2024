# Serializers Documentation

## WarriorSerializer

This serializer is used to serialize the `Warrior` model.

### Fields

- `id`: Auto-generated unique identifier for the warrior.
- `race`: Character field representing the race of the warrior.
- `name`: Character field for the name of the warrior.
- `level`: Integer field representing the level of the warrior.
- `skill`: Many-to-Many relationship field with the `Skill` model through the `SkillOfWarrior` intermediate model.
- `profession`: Foreign key relationship field with the `Profession` model, representing the profession of the warrior.

## ProfessionSerializer

This serializer is used to serialize the `Profession` model.

### Fields

- `id`: Auto-generated unique identifier for the profession.
- `title`: Character field for the title of the profession.
- `description`: Text field for the description of the profession.

## SkillSerializer

This serializer is used to serialize the `Skill` model.

### Fields

- `id`: Auto-generated unique identifier for the skill.
- `title`: Character field for the title of the skill.

## WarriorWithProfessionSerializer

This serializer is used to serialize the `Warrior` model along with its associated `Profession`.

### Fields

- `id`: Auto-generated unique identifier for the warrior.
- `race`: Character field representing the race of the warrior.
- `name`: Character field for the name of the warrior.
- `level`: Integer field representing the level of the warrior.
- `skill`: Many-to-Many relationship field with the `Skill` model through the `SkillOfWarrior` intermediate model.
- `profession`: Nested serialization of the `Profession` model.

## RetrieveWarriorSerializer

This serializer is used to serialize the `Warrior` model along with its associated `Profession` and `Skill`.

### Fields

- `id`: Auto-generated unique identifier for the warrior.
- `race`: Character field representing the race of the warrior.
- `name`: Character field for the name of the warrior.
- `level`: Integer field representing the level of the warrior.
- `skill`: Nested serialization of the `Skill` model (many=True).
- `profession`: Nested serialization of the `Profession` model.

## WarriorWithSkillSerializer

This serializer is used to serialize the `Warrior` model along with its associated `Skill`.

### Fields

- `id`: Auto-generated unique identifier for the warrior.
- `race`: Character field representing the race of the warrior.
- `name`: Character field for the name of the warrior.
- `level`: Integer field representing the level of the warrior.
- `skill`: Nested serialization of the `Skill` model (many=True).
