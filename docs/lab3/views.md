## Views 

В ходе выполнения работы были реализованы все views, необходимые для успешного создания полного функционала лабораторной работы. Более подробно рассмотреть views можно в коде в папке лабораторной.

### Пример:

- ViewSet, который показывает все места для зимовки животных, используя для этого данные сериалайзера WinterPlaceSerializer и модель WinterPlace. Таким образом, можно посмотреть все WinterPlace. Также реализована функция проверки метода для избежания неавторизованного вмешательства в базу. 

```python
class WinterPlaceViewSet(ModelViewSet):
    queryset = WinterPlace.objects.all()
    serializer_class = serializers.WinterPlaceSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]
```