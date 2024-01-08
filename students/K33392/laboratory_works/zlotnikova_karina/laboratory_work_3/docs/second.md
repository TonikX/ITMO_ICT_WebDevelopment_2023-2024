# Калькулятор калорий.

###### Расчет суточной нормы калорий по полу, весу, росту и возрасту

```
class CountViewSet(ViewSet):
    @extend_schema(request=InCalculateSerializer, responses={"norm_of_calories": int}) #дока для сваггера (определяет как внешний вид и поля сваггера)
    @action(detail=False, methods=["POST"]) 
    def calculate(self, request):
        sex = request.data.get('sex', None)
        tall = request.data.get('tall', None)
        w = request.data.get('weight', None)
        age = request.data.get('age', None)
        res = 0
        if sex == 'female':
            res = ((10 * w) + (6.25 * tall) - (5 * age) - 161)
        elif sex == 'male':
            res = ((10 * w) + (6.25 * tall) - (5 * age) + 5)
        else:
            return Response('sex is not valid', status=status.HTTP_400_BAD_REQUEST)

        return Response({"norm_of_calories": math.ceil(res)}, status=status.HTTP_200_OK)

```

###### Сериалайзер

```
class InCalculateSerializer(serializers.Serializer): #просто задаем данные о юзере
    sex = serializers.ChoiceField(choices=['male', 'female'], default='male')
    tall = serializers.IntegerField(default=0)
    weight = serializers.IntegerField(default=0)
    age = serializers.IntegerField()

    class Meta:
        fields = ['sex', 'tall', 'weight', 'age']

```