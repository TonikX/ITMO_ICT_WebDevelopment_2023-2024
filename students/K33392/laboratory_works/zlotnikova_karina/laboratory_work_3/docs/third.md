# Дневник калорий.

Записываем что во сколько и когда съел пользователь и сколько калорий это принесло.


###### Необходимые модели продукта, дня и съеденного.
```
class Product(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField()


class Day(models.Model):
    date = models.DateField()


class Eaten(models.Model):
    product = models.ForeignKey(Product, related_name='what_eaten', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='who_eat', on_delete=models.CASCADE)
    when_date = models.ForeignKey(Day, related_name='eaten', on_delete=models.CASCADE)
    when_time = models.TimeField()

```
###### Сериалайзеры
```
from rest_framework import serializers
from .models import CustomUser, Product, Eaten, Day
import datetime


class ProductSerializer(serializers.ModelSerializer): #работа с полями продукта
    class Meta:
        model = Product
        fields = '__all__'


class EatenSerializer(serializers.ModelSerializer): #работа со съеденным (используется для отображения)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Eaten
        fields = ['product', 'when_time']


class CreateEatenSerializer(serializers.ModelSerializer): #работа со съеденным (создание серилайзера)
    class Meta:
        model = Eaten
        fields = ['product']

    def create(self, request):
        date = datetime.date.today()
        date_obj, _ = Day.objects.get_or_create(date=date) #создание записи, если ее ранее не было (дата)
        time = datetime.datetime.now().time()

        product = Product.objects.get(id=self.data['product']) #только если тестовая версия и id - это PK

        obj = Eaten.objects.create(product=product,
                                   user=self.context["user"],
                                   when_date=date_obj,
                                   when_time=time)
        return obj


class DaySerializer(serializers.ModelSerializer):

    left = serializers.SerializerMethodField()
    eaten = serializers.SerializerMethodField()

    class Meta:
        model = Day
        fields = ['date', 'left', 'eaten']

    def get_left(self, obj):
        user = self.context["user"]
        products_ids = Eaten.objects.filter(when_date=obj, user=user).values_list('product', flat=True) #получаем список съеденных продуктов
        eaten_cols = 0
        for product in Product.objects.filter(id__in=products_ids): #вычисляем сумму калорий съеденных за день продуктов
            eaten_cols += product.calories 

        return user.norm_cal - eaten_cols

    def get_eaten(self, obj): #сериализированные данные о съеденных подуктах
        user = self.context["user"]
        qs_eaten = Eaten.objects.filter(when_date=obj, user=user)
        ser = EatenSerializer(qs_eaten, many=True)
        return ser.data


class CreateDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['date']


class ProfileSerializer(serializers.ModelSerializer): #отображение данных о пользователе

    products = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'norm_cal', 'products']

    def get_products(self, obj): #возвращаем данные для страницы дневника калорий
        dates = Eaten.objects.filter(user=obj).values_list('when_date', flat=True)
        qs_date = Day.objects.filter(id__in=dates)
        ser = DaySerializer(qs_date, many=True, context={"user": obj})
        return ser.data

```

######  Вывод съеденных продуктов
```
class EatenViewSet(GenericViewSet):
    queryset = Eaten.objects.all()
    serializer_class = CreateEatenSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        ser = self.get_serializer(data=request.data, context={"user": request.user})
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_201_CREATED)

```
