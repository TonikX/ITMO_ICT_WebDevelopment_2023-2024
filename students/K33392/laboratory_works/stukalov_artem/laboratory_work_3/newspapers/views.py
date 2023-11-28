from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max, Sum
from . import models
from . import serializers


class NewspaperViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.Newspaper.objects.all()
    serializer_class = serializers.NewspaperSerializer


class PrintingOfficeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.PrintingOffice.objects.all()
    serializer_class = serializers.PrintingOfficeSerializer


class PostOfficeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.PostOffice.objects.all()
    serializer_class = serializers.PostOfficeSerializer


class NewspaperEditionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.NewspaperEdition.objects.all()
    serializer_class = serializers.NewspaperEditionSerializer


class NewspaperOrderViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.NewspaperOrder.objects.all()
    serializer_class = serializers.NewspaperOrderSerializer


class NewspaperDistributionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.NewspaperDistribution.objects.all()
    serializer_class = serializers.NewspaperDistributionSerializer


@api_view(["POST"])
@permission_classes([IsAdminUser])
def find_printing_addresses_by_name(request):
    name = request.data["name"]
    queryset = models.NewspaperEdition.objects.filter(newspaper__name=name)
    res = serializers.NewspaperEditionAddresSerializer(queryset, many=True)
    return Response(res.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def most_printed_author(request):
    pk = request.data["id"]
    queryset = (
        models.NewspaperEdition.objects.filter(printing_office__pk=pk)
        .values("newspaper__name", "newspaper__redactor_full_name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
        .first()
    )
    res = {
        "name": queryset["newspaper__name"],
        "author": queryset["newspaper__redactor_full_name"],
        "count": queryset["total"],
    }
    return Response(res, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def distribution_addresses_by_price(request):
    price = request.data["price"]
    queryset = (
        models.NewspaperDistribution.objects.filter(edition__newspaper__price__gt=price)
        .values("post_office__address")
        .distinct()
    )
    res = {"addresses": list(map(lambda ob: ob["post_office__address"], queryset))}
    return Response(res, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def less_count_distribution_addresses(request):
    distributed_newspapers = models.NewspaperDistribution.objects.values(
        "edition__newspaper__name", "post_office__index"
    ).annotate(total=Sum("amount"))

    required_newspapers = models.NewspaperOrder.objects.values(
        "newspaper__name", "post_office__index"
    ).annotate(total=Sum("amount"))

    distributed_newspapers_dict = {}
    for distributed in distributed_newspapers:
        key = (
            distributed["edition__newspaper__name"],
            distributed["post_office__index"],
        )
        distributed_newspapers_dict[key] = distributed["total"]

    lost_orders = {}
    for required in required_newspapers:
        key = (required["newspaper__name"], required["post_office__index"])

        diff = required["total"] - distributed_newspapers_dict.get(key, 0)

        if diff <= 0:
            continue

        if key[1] not in lost_orders:
            lost_orders[key[1]] = {}

        lost_orders[key[1]][key[0]] = diff

    return Response(lost_orders, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def newspaper_distribution_addresses(request):
    name = request.data["name"]
    address = request.data["address"]
    queryset = (
        models.NewspaperDistribution.objects.filter(
            edition__newspaper__name=name, edition__printing_office__address=address
        )
        .values("post_office__address")
        .distinct()
    )
    res = {"addresses": list(map(lambda ob: ob["post_office__address"], queryset))}
    return Response(res, status=status.HTTP_200_OK)
