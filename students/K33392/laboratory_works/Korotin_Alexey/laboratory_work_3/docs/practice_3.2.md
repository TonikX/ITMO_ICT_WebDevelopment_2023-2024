# Практика 3.2
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
class WarriorSkillsAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"skills": serializer.data})

    def post(self, request):
        skill = request.data
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)
```

Один view обрабатывает получение get и post запросов на один и тот же URL

## URLS 

```python
urlpatterns = [
    path("warriors/skills", WarriorSkillsAPIView.as_view()),
]
```

# Задание 2 - Реализовать эндпоинты
## Вывод полной информации о всех войнах и их профессиях (в одном запросе).
### API view
```python
class WarriorProfessionListAPIView(ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()
```
### Serializer 

```python
class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        exclude = ('skill', )
```
### URL
```python
path("warriors/profession", WarriorProfessionListAPIView.as_view())
```
## Вывод полной информации о всех войнах и их скилах (в одном запросе).
### API view
```python
class WarriorSkillListApiView(ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()
```
### Serializer 

```python
class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        exclude = ('profession', )
```
### URL
```python
path("warriors/skill", WarriorSkillListApiView.as_view()),
```

## Вывод полной информации о войне (по id), его профессиях и скилах.
### API view
```python
class GetWarriorAPIView(RetrieveAPIView):
    serializer_class = FullWarriorSerializer
    queryset = Warrior.objects.all()
```
### Serializer 

```python
class FullWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    profession = ProfessionSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"

```
### URL
```python
    path("warriors/<int:pk>", GetWarriorAPIView.as_view()),
```

## Удаление война по id.
### API view
```python
class DeleteWarriorAPIView(DestroyAPIView):
    serializer_class = FullWarriorSerializer
    queryset = Warrior.objects.all()
```
### URL
```python
path("warriors/<int:pk>/delete", DeleteWarriorAPIView.as_view()),
```
## Редактирование информации о войне.
### API view
```python
class UpdateWarriorAPIView(UpdateAPIView):
    serializer_class = FullWarriorSerializer
    queryset = Warrior.objects.all()
```
### URL
```python
path("warriors/<int:pk>/update", UpdateWarriorAPIView.as_view()),
```
