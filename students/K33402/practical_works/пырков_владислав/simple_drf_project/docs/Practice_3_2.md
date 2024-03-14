
# Задание 1
Реализовать ендпоинты для добавления и просмотра скилов воинов
## Сериалайзер

```python
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
```

## API view

```python
class SkillAPIView(APIView):
   def get(self, request):
       skills = Skill.objects.all()
       serializer = SkillSerializer(skills, many=True)
       return Response({"Skills": serializer.data})

class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill_model_inst = Skill(**validated_data)
        skill_model_inst.save()
        return skill_model_inst

    def update(self, instance, validated_data):
        pass
```

## URLS 

```python
path('skills/', SkillAPIView.as_view()),
path('skill/create/', SkillCreateView.as_view()),
```

# Задание 2 - Реализовать эндпоинты
## Вывод полной информации о всех войнах и их профессиях (в одном запросе).

### Serializer 

```python
class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(many=False)
    class Meta:
        model = Warrior
        fields = ["id", "race", "name", "level", "profession"]
```
### API view
```python
class WarriorProfessionListAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()
```
### URLS
```python
path("warriors/profession/", WarriorProfessionListAPIView.as_view()),
```
## Вывод полной информации о всех войнах и их скиллах (в одном запросе).

### Serializer 

```python
class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = ["id", "race", "name", "level", "skill"]
```
### API view
```python
class WarriorSkillListApiView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()
```

### URLS
```python
path("warriors/skill/", WarriorSkillListApiView.as_view()),
```

## Вывод полной информации о войне (по id), его профессиях и скилах.

### Serializer 

```python
class OneWarriorSerializer(serializers.ModelSerializer,):
    skill = SkillSerializer(many=True)
    profession = ProfessionSerializer(many=False)

    class Meta:
        model = Warrior
        fields = "__all__"

```
### API view
```python
class ShowWarriorAPIView(generics.RetrieveAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()
```

### URLS
```python
    path('warriors/<int:pk>/', ShowWarriorAPIView.as_view()),
```

## Удаление война по id.
### API view
```python
class DeleteWarriorAPIView(generics.DestroyAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()

```
### URLS
```python
path("warriors/delete/<int:pk>/", DeleteWarriorAPIView.as_view()),
   
```
## Редактирование информации о войне.
### API view
```python
class UpdateWarriorAPIView(UpdateAPIView):
    serializer_class = OneWarriorSerializer
    queryset = Warrior.objects.all()
```
### URLS
```python
path("warriors/update/<int:pk>/", UpdateWarriorAPIView.as_view()),
```