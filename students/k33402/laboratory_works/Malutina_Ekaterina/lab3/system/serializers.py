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
