from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Newspaper, PrintingHouse, PostOffice, NewspaperPrint, NewspaperArrival, NewspaperOrder, UserProfile
from .serializers import NewspaperSerializer, PrintingHouseSerializer, PostOfficeSerializer, NewspaperPrintSerializer, NewspaperArrivalSerializer, NewspaperOrderSerializer, UserProfileSerializer

class NewspaperListCreateView(generics.ListCreateAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    permission_classes = [IsAuthenticated]

class NewspaperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    permission_classes = [IsAuthenticated]

class PrintingHouseListCreateView(generics.ListCreateAPIView):
    queryset = PrintingHouse.objects.all()
    serializer_class = PrintingHouseSerializer
    permission_classes = [IsAuthenticated]

class PrintingHouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrintingHouse.objects.all()
    serializer_class = PrintingHouseSerializer
    permission_classes = [IsAuthenticated]

class PostOfficeListCreateView(generics.ListCreateAPIView):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer
    permission_classes = [IsAuthenticated]

class PostOfficeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer
    permission_classes = [IsAuthenticated]

class NewspaperPrintListCreateView(generics.ListCreateAPIView):
    queryset = NewspaperPrint.objects.all()
    serializer_class = NewspaperPrintSerializer
    permission_classes = [IsAuthenticated]

class NewspaperPrintDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewspaperPrint.objects.all()
    serializer_class = NewspaperPrintSerializer
    permission_classes = [IsAuthenticated]

class NewspaperArrivalListCreateView(generics.ListCreateAPIView):
    queryset = NewspaperArrival.objects.all()
    serializer_class = NewspaperArrivalSerializer
    permission_classes = [IsAuthenticated]

class NewspaperArrivalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewspaperArrival.objects.all()
    serializer_class = NewspaperArrivalSerializer
    permission_classes = [IsAuthenticated]

class NewspaperOrderListCreateView(generics.ListCreateAPIView):
    queryset = NewspaperOrder.objects.all()
    serializer_class = NewspaperOrderSerializer
    permission_classes = [IsAuthenticated]

class NewspaperOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewspaperOrder.objects.all()
    serializer_class = NewspaperOrderSerializer
    permission_classes = [IsAuthenticated]

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]