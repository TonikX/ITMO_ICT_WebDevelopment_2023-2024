# Лабораторная работа 3:

## Реализация серверной части приложения средствами DJANGO и Django REST Framework

**Дисциплина:** Основы web-программирования

**Цель:** овладеть практическими навыками и умениями реализации web-сервисов
средствами Django.

**Оборудование:** компьютерный класс.

**Программное обеспечение:** Python 3.6+, Django 3, Django REST Framework (DRF), PostgreSQL \*.

**Практическое задание:** Реализовать сайт, используя фреймворк Django 3, Django REST Framework, Djoser и
СУБД PostgreSQL \*, в соответствии с вариантом задания лабораторной работы.

**Вариант - Калькулятор калорий:**

Разработка инструмента для расчета суточной нормы калорий с учетом введенных пользователем данных о поле, возрасте, росте, весе и уровне физической активности. Функционал:

- Регистрация и авторизация по токенам/ вывод информации о текущем
  пользователе средствами Djoser.
- Подсчет суточной нормы калорий для юзера.
- Запись ежедневного потребления калорий (с указанием продуктов) и отображение прогресса по дням и времени.

# Регистрация и авторизация по токенам/ вывод информации о текущем пользователе средствами Djoser.

###### settings.py

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

```

###### utils.py

```
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

```

###### Модель кастомного менеджера

```
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


```

###### Модель пользователя

```
class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    id = models.BigAutoField(primary_key=True)

    norm_cal = models.FloatField(default=0.0, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    linkedin_token = models.TextField(blank=True, default='')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    avatar = models.ImageField(default='default.png')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
```

###### Сериалайзер регистрации

```
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)


```

```
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()
```

###### Вывод информации о юзере

```
class ProfileViewSet(GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["GET"])
    def me(self, request):
        obj = request.user
        ser = ProfileSerializer(obj)
        return Response(ser.data)
```

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

###### Вывод съеденных продуктов

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
