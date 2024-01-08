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


class InCalculateSerializer(serializers.Serializer): #просто задаем данные о юзере
    sex = serializers.ChoiceField(choices=['male', 'female'], default='male')
    tall = serializers.IntegerField(default=0)
    weight = serializers.IntegerField(default=0)
    age = serializers.IntegerField()

    class Meta:
        fields = ['sex', 'tall', 'weight', 'age']

####################################


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


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password',]


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = []


class PasswordChangeSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = CustomUser
        fields = ['current_password', 'new_password']

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value
