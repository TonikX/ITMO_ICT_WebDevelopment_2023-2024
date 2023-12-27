from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from .models import (CustomUser,
                     Newspaper,
                     Printer,
                     PrintingNewspaper,
                     PostOffice,
                     PostOfficeOrder,
                     Transportation)


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'type', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password',]


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


###################################################

class NewspaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newspaper
        fields = '__all__'


class PostOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOffice
        fields = '__all__'


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'


class PrintingNewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintingNewspaper
        fields = '__all__'


class ShowPrintingNewspaperSerializer(serializers.ModelSerializer):
    newspaper = NewspaperSerializer(read_only=True)
    printer = PrinterSerializer(read_only=True)

    class Meta:
        model = PrintingNewspaper
        fields = ['id', 'newspaper', 'printer', 'how_many_to_print']


class PostOfficeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOfficeOrder
        fields = '__all__'


class ShowPostOfficeOrderSerializer(serializers.ModelSerializer):
    newspaper = NewspaperSerializer(read_only=True)
    post_office = PostOfficeSerializer(read_only=True)

    class Meta:
        model = PostOfficeOrder
        fields = ['id', 'newspaper', 'post_office', 'how_many_needed']


class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = '__all__'


class ShowTransportationSerializer(serializers.ModelSerializer):
    printing_newspaper = ShowPrintingNewspaperSerializer(read_only=True)
    post_office_order = ShowPostOfficeOrderSerializer(read_only=True)

    class Meta:
        model = Transportation
        fields = ['id', 'printing_newspaper', 'post_office_order', 'amount']


class ShowLossSerializer(serializers.ModelSerializer):

    have = serializers.SerializerMethodField()
    newspaper = NewspaperSerializer(read_only=True)
    post_office = PostOfficeSerializer(read_only=True)

    class Meta:
        model = PostOfficeOrder
        fields = ['id', 'newspaper', 'post_office', 'how_many_needed', 'have']

    @extend_schema_field(OpenApiTypes.INT)
    def get_have(self, obj):
        return self.context[obj.id]['amount__sum']


class ShowRedactor(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ['redactor_last_name', 'redactor_first_name', 'redactor_patronic']


class ShowPrintingAddreses(serializers.ModelSerializer):

    address = serializers.CharField(source='printer.address')

    class Meta:
        model = PrintingNewspaper
        fields = ['address']


class FindTransportationsSerializers(serializers.Serializer):

    name = serializers.CharField()
    where_printed = serializers.CharField()

    class Meta:
        fields = ['name', 'where_printed']


class ShowTransportEndSerializer(serializers.ModelSerializer):
    post_needed = ShowPostOfficeOrderSerializer(read_only=True)
    class Meta:
        model = Transportation
        fields = ['post_needed']

