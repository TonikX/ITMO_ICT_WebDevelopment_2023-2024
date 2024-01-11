## Serializers 

В ходе выполнения работы были реализованы все сериалайзеры, необходимые для успешного создания полного функционала лабораторной работы. Более подробно рассмотреть сериалайзеры можно в коде в папке лабораторной.

### Пример:

- Сериалайзер, выступающий за подсчет животных в вольере. На выходе предоставляются id вольера, его название, количество животных и сами животные, взятые из модели по фильтру условия. 

```python
class CountAnimalInArea(serializers.ModelSerializer):

    count_animals_in = serializers.SerializerMethodField()
    animals_in = serializers.SerializerMethodField()

    def get_count_animals_in(self, obj):
        aias = AnimalInAviary.objects.filter(aviary__building__area=obj.id)
        return Animal.objects.filter(where__in=aias).distinct().count()

    def get_animals_in(self, obj):
        aias = AnimalInAviary.objects.filter(aviary__building__area=obj.id)
        qs = Animal.objects.filter(where__in=aias).distinct()
        ser = AnimalSerializer(qs, many=True)
        return ser.data

    class Meta:
        model = Area
        fields = ['id', 'name', 'count_animals_in', 'animals_in']
```