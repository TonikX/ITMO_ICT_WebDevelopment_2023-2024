# System

## apps.py
```python
from django.apps import AppConfig


class SystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'system'
```

## models.py
```python
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


# модель менеджера
class CustomUserManager(BaseUserManager):
    # создание пользователя
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    # создание админа
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# модель пользователя
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

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


# модель продукта
class Product(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField()


# модель даты
class Day(models.Model):
    date = models.DateField()


# модель съеденного
class Eaten(models.Model):
    product = models.ForeignKey(Product, related_name='what_eaten', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='who_eat', on_delete=models.CASCADE)
    when_date = models.ForeignKey(Day, related_name='eaten', on_delete=models.CASCADE)
    when_time = models.TimeField()
```

## serializers.py
```python
from rest_framework import serializers
from .models import CustomUser, Product, Eaten, Day
import datetime


# парсинг и кодирование продукта
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# отображение съеденного
class EatenSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Eaten
        fields = ['product', 'when_time']


# создание съеденного
class CreateEatenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eaten
        fields = ['product']

    def create(self, request):
        date = datetime.date.today()
        # создание записи, если ее ранее не было (дата)
        date_obj, _ = Day.objects.get_or_create(date=date)
        time = datetime.datetime.now().time()

        # только если тестовая версия и id первичный ключ
        product = Product.objects.get(id=self.data['product'])

        obj = Eaten.objects.create(product=product, user=self.context["user"], when_date=date_obj, when_time=time)
        return obj


class DaySerializer(serializers.ModelSerializer):
    left = serializers.SerializerMethodField()
    eaten = serializers.SerializerMethodField()

    class Meta:
        model = Day
        fields = ['date', 'left', 'eaten']

    def get_left(self, obj):
        user = self.context["user"]
        # получаем список съеденных продуктов
        products_ids = Eaten.objects.filter(when_date=obj, user=user).values_list('product', flat=True)
        eaten_cols = 0
        # считаем калории
        for product in Product.objects.filter(
                id__in=products_ids):
            eaten_cols += product.calories

        return user.norm_cal - eaten_cols

    # получение данных о съеденных продуктах
    def get_eaten(self, obj):
        user = self.context["user"]
        qs_eaten = Eaten.objects.filter(when_date=obj, user=user)
        ser = EatenSerializer(qs_eaten, many=True)
        return ser.data


class CreateDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['date']


# отображение пользовательских данных
class ProfileSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'norm_cal', 'products']

    # получаем данные дневника калорий
    def get_products(self, obj):
        dates = Eaten.objects.filter(user=obj).values_list('when_date', flat=True)
        qs_date = Day.objects.filter(id__in=dates)
        ser = DaySerializer(qs_date, many=True, context={"user": obj})
        return ser.data


class InCalculateSerializer(serializers.Serializer):  # просто задаем данные о юзере
    sex = serializers.ChoiceField(choices=['male', 'female'], default='male')
    tall = serializers.IntegerField(default=0)
    weight = serializers.IntegerField(default=0)
    age = serializers.IntegerField()

    class Meta:
        fields = ['sex', 'tall', 'weight', 'age']


# регистрация
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password_confirmation = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError("passwords does not match")
        return attrs

    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)


# авторизация
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


# выход из системы
class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = []


# смена пароля
class PasswordChangeSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = CustomUser
        fields = ['current_password', 'new_password']

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'does not match'})
        return value
```

## urls.py
```python
from . import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('profile', viewset=views.ProfileViewSet)
router.register('product', viewset=views.ProductViewSet)
router.register('eaten', viewset=views.EatenViewSet)
router.register('calculator', viewset=views.CountViewSet, basename='calculator')


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),

    path('', include(router.urls)),
]
```

## utils.py
```python
from rest_framework_simplejwt.tokens import RefreshToken


# получение токенов
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}
```

## views.py
```python
import math

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework import generics
from .utils import get_tokens_for_user
from .serializers import *
from .models import CustomUser, Product, Eaten
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_spectacular.utils import extend_schema


# представление подсчета калорий
class CountViewSet(ViewSet):
    @extend_schema(request=InCalculateSerializer, responses={"norm_of_calories": int})    # сваггер
    @action(detail=False, methods=["POST"])
    def calculate(self, request):
        sex = request.data.get('sex', None)
        tall = request.data.get('tall', None)
        w = request.data.get('weight', None)
        age = request.data.get('age', None)
        if sex == 'female':
            res = ((10 * w) + (6.25 * tall) - (5 * age) - 161)
        elif sex == 'male':
            res = ((10 * w) + (6.25 * tall) - (5 * age) + 5)
        else:
            return Response('sex is not valid', status=status.HTTP_400_BAD_REQUEST)

        return Response({"norm_of_calories": math.ceil(res)}, status=status.HTTP_200_OK)


# представление профиля
class ProfileViewSet(GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["GET"])
    def me(self, request):
        obj = request.user
        ser = ProfileSerializer(obj)
        return Response(ser.data)


# представление продукта
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]  # сравнение токенов в бд и того, который пришел с запроса
        return [IsAdminUser()]


# представление съеденного
class EatenViewSet(GenericViewSet):
    queryset = Eaten.objects.all()
    serializer_class = CreateEatenSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        ser = self.get_serializer(data=request.data, context={"user": request.user})
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_201_CREATED)


# представление регистрации
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()


# представление авторизации
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        if email is not None and password is not None:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# представление выхода из аккаунта
class LogoutView(APIView):
    serializer_class = LogoutSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        logout(request)
        return Response({'msg': 'successfully logged out'}, status=status.HTTP_200_OK)


# представление смены пароля
class ChangePasswordView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # equals Line 17
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
```