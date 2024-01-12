from rest_framework import generics
from .serializers import *
from .models import *
from django.db.models import Count, F


class FoundationListView(generics.ListAPIView):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer


class CardListView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardCreateAPIView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardCreateSerializer


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCreateAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateSerializer


class ExhibitionListView(generics.ListAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer


class ExhibitionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = FoundationSerializer


class CardToFoundationListView(generics.ListAPIView):
    queryset = CardToFoundation.objects.all()
    serializer_class = CardToFoundationSerializer


class ItemToExhibitionListView(generics.ListAPIView):
    queryset = ItemToExhibition.objects.all()
    serializer_class = ItemToExhibitionSerializer


class CardToFoundationCreateAPIView(generics.CreateAPIView):
    queryset = CardToFoundation.objects.all()
    serializer_class = CardToFoundationCreateSerializer


class ItemToExhibitionCreateAPIView(generics.CreateAPIView):
    queryset = ItemToExhibition.objects.all()
    serializer_class = ItemToExhibitionCreateSerializer


class FoundationExhibitionCountView(generics.ListAPIView):
    queryset = Foundation.objects.annotate(num_exhibitions=Count('card__item__exhibition', distinct=True))
    serializer_class = FoundationExhibitionSerializer


class CardItemCountView(generics.ListAPIView):
    queryset = Card.objects.annotate(num_items=Count('item', distinct=True))
    serializer_class = CardItemSerializer


class FoundationRatioView(generics.ListAPIView):
    total_cards = Card.objects.count()
    queryset = Foundation.objects.annotate(num_cards=Count('card')).annotate(
        percentage=F('num_cards') * 100 / total_cards)
    serializer_class = FoundationRatioSerializer


class ItemCommonExhibitionsView(generics.ListAPIView):
    serializer_class = ItemCommonExhibitionsSerializer

    def get_queryset(self):
        item_id = self.kwargs['pk']
        specified_item = Item.objects.get(id=item_id)
        queryset = Item.objects.filter(exhibition__in=specified_item.exhibition.all()).exclude(id=specified_item.id).distinct()
        return queryset
