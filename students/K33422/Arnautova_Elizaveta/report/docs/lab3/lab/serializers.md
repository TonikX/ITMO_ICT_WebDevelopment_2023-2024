**Serializers:** 

Горы:
```
class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = "__all__"
        # fields = ["name", "height", "country", "region"]
```

Альпинисты:
```
class ClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        # fields = ['first_name', 'last_name', "birth_date"]
        fields = "__all__"
```

Восхождения:
```
class AscensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ascension
        # fields = "__all__"
        fields = ["route_id", "start_date", "planned_end_date", "actual_end_date", "comment"]
```

Клубы:
```
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"
```

**Теперь к чуть более интересному:**

Сериализатор, наследующий информацию от одного из указанных выше и сериализатора групп.
```
class AscentParticipationSerializer(serializers.ModelSerializer):
    group_id = GroupGetSerializer()
    climber_id = ClimberSerializer()

    class Meta:
        model = AscentParticipation
        fields = "__all__"
```

Два сериализатора для групп. 

Один -- чтобы просто получить список и вывести его:
```
class GroupGetSerializer(serializers.ModelSerializer):
    climbers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = "__all__"
```

Второй, который связывается через первичный ключ с таблицей альпинистов, чтобы, если что, редактировать список членов группы:
```
class GroupPostSerializer(serializers.ModelSerializer):
    climbers = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Climber.objects.all())
    class Meta:
        model = Group
        fields = "__all__"
```

