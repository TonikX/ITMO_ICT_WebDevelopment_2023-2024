# warriors_app/serializers.py

Этот файл отвечает за сериализацию (преобразование данных в формат, пригодный для передачи по сети) моделей моего проекта в Django REST Framework.

## ProfessionCreateSerializer

```python
from rest_framework import serializers
from .models import Profession

class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"
```
Описание: Этот сериализатор используется для преобразования данных модели Profession в формат, понятный для работы с API. Он включает в себя все поля модели.



## WarriorWithProfessionSerializer
```python
from rest_framework import serializers
from .models import Profession
from .models import Warrior, Skill, SkillOfWarrior, Profession


class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"
```	
Описание: Этот сериализатор связывает данные модели Warrior с данными модели Profession. Поле profession представлено в формате, описанном в ProfessionCreateSerializer.

## WarriorWithSkillsSerializer
```python

class WarriorWithProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"
```
Описание: Этот сериализатор включает в себя навыки воина, представленные в виде строк, и используется для преобразования данных модели Warrior в формат, удобный для API.

## WarriorWithSkillsSerializer

```python
class WarriorWithSkillsSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"
```
Описание: Этот сериализатор используется для преобразования данных модели Warrior в формат, пригодный для API. Поле skills представлено в виде строк, и оно включает в себя умения, которыми владеет воин.


