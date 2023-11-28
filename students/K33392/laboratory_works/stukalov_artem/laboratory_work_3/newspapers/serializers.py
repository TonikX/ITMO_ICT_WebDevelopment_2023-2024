from rest_framework.serializers import ModelSerializer, CharField
from . import models


class NewspaperSerializer(ModelSerializer):
    class Meta:
        model = models.Newspaper
        fields = "__all__"


class PrintingOfficeSerializer(ModelSerializer):
    class Meta:
        model = models.PrintingOffice
        fields = "__all__"


class PostOfficeSerializer(ModelSerializer):
    class Meta:
        model = models.PostOffice
        fields = "__all__"


class NewspaperEditionSerializer(ModelSerializer):
    newspaper = NewspaperSerializer()
    printing_office = PrintingOfficeSerializer()

    class Meta:
        model = models.NewspaperEdition
        fields = "__all__"


class NewspaperOrderSerializer(ModelSerializer):
    newspaper = NewspaperSerializer()
    post_office = PostOfficeSerializer()

    class Meta:
        model = models.NewspaperOrder
        fields = "__all__"


class NewspaperDistributionSerializer(ModelSerializer):
    edition = NewspaperEditionSerializer()
    post_office = PostOfficeSerializer()

    class Meta:
        model = models.NewspaperDistribution
        fields = "__all__"


class NewspaperEditionAddresSerializer(ModelSerializer):
    address = CharField(source="printing_office.address")

    class Meta:
        model = models.NewspaperEdition
        fields = ["address"]
