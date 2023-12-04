from django.shortcuts import render
from rest_framework import generics
from .models import Museum, Author, Set, Item, Foundation, Exhibition, ItemToExhibition, SetToFoundation
from .serializers import MuseumSerializer, AuthorSerializer, SetSerializer, ItemSerializer, FoundationSerializer,\
    ExhibitionSerializer, ItemToExhibitionSerializer, SetToFoundationSerializer

class MuseumListView(generics.ListCreateAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer

class MuseumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer

class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SetListView(generics.ListAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class FoundationListView(generics.ListCreateAPIView):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer

class FoundationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer

class ExhibitionListView(generics.ListCreateAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer

class ExhibitionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
