from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class CreateReaderAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateBookAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookInstanceAPIView(ListAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()


class CreateInstanceAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()


class OneBookAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class OneInstanceAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()


class ReaderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class BookTakingAPIView(APIView):
    def post(self, request):
        serializer = BookTakingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class BookTakingListAPIView(ListAPIView):
    serializer_class = BookTakingSerializer
    queryset = BookTaking.objects.all()


class BookTakingPostAPIView(CreateAPIView):
    serializer_class = BookTakingSerializer
    queryset = BookTaking.objects.all()


class BookTakingDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookTakingSerializer
    queryset = BookTaking.objects.all()

class ReaderInfoAPIView(APIView):
    def get(self, request):
        count_lt_20_years = Reader.objects.filter(birth_date__year__gt=timezone.now().year - 20).count()
        educations = Reader.objects.all().values('education').annotate(
            count=Count('id')
        ).order_by()
        percents = {}
        count_readers = Reader.objects.count()
        for education in educations:
            percents[education['education']] = education['count'] / count_readers * 100
        return Response({'percents': percents, 'count_lt_20_years': count_lt_20_years})
