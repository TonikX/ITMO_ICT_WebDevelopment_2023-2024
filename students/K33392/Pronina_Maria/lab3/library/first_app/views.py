from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HallListView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallRetrieveView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallUpdateView(generics.UpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallCreateView(generics.CreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class CopyListView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyRetrieveView(generics.RetrieveAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyUpdateView(generics.UpdateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CreateCopySerializer


class CopyCreateView(generics.CreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CreateCopySerializer


class ReaderListView(generics.ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderRetrieveView(generics.RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderUpdateView(generics.UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = CreateReaderSerializer


class ReaderCreateView(generics.CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = CreateReaderSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentRetrieveView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentUpdateView(generics.UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = CreateAssignmentSerializer


class AssignmentCreateView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = CreateAssignmentSerializer
