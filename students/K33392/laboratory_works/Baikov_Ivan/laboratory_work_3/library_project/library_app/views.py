from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from library_app.models import Book, Hall, Reader, Ownership, Availability
from library_app.serializers import BookSerializer, HallSerializer, ReaderSerializer, OwnershipSerializer, \
    AvailabilitySerializer, GoodBookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, ]



class HallListView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class HallRetrieveView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class HallCreateView(generics.CreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class HallUpdateView(generics.UpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class HallDeleteView(generics.DestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, ]



class ReaderListView(generics.ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ReaderRetrieveView(generics.RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ReaderCreateView(generics.CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ReaderUpdateView(generics.UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ReaderDeleteView(generics.DestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, ]



class OwnershipListView(generics.ListAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class OwnershipRetrieveView(generics.RetrieveAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class OwnershipCreateView(generics.CreateAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class OwnershipUpdateView(generics.UpdateAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class OwnershipDeleteView(generics.DestroyAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_classes = [permissions.IsAuthenticated, ]



class AvailabilityListView(generics.ListAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, ]

class AvailabilityRetrieveView(generics.RetrieveAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, ]

class AvailabilityCreateView(generics.CreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, ]

class AvailabilityUpdateView(generics.UpdateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, ]

class AvailabilityDeleteView(generics.DestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, ]

class LogOut(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class GoodBookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = GoodBookSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class AvailableBooks(generics.ListAPIView):

    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    def get_queryset(self):
       reader = self.kwargs['reader']
       reader = Reader.objects.get(pk=reader)
       books = reader.hall.books
       return books
