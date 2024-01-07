from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from .models import Newspaper, PrintingHouse, PostOffice, NewspaperPrint, NewspaperArrival, NewspaperOrder, UserProfile
from .serializers import NewspaperSerializer, PrintingHouseSerializer, PostOfficeSerializer, NewspaperPrintSerializer, NewspaperArrivalSerializer, NewspaperOrderSerializer, UserProfileSerializer

@csrf_exempt
def get_newspapers(request):
    temp = Newspaper.objects.all()
    serializer = NewspaperSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class NewspaperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
    
    
@csrf_exempt
def get_printinghouses(request):
    temp = PrintingHouse.objects.all()
    serializer = PrintingHouseSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class PrintingHouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrintingHouse.objects.all()
    serializer_class = PrintingHouseSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
    

@csrf_exempt
def get_postoffices(request):
    temp = PostOffice.objects.all()
    serializer = PostOfficeSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class PostOfficeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
    

@csrf_exempt
def get_newspaperprints(request):
    temp = NewspaperPrint.objects.all()
    serializer = NewspaperPrintSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class NewspaperPrintDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewspaperPrint.objects.all()
    serializer_class = NewspaperPrintSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
    

@csrf_exempt
def get_newspaperarrivals(request):
    temp = NewspaperArrival.objects.all()
    serializer = NewspaperArrivalSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class NewspaperArrivalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewspaperArrival.objects.all()
    serializer_class = NewspaperArrivalSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
    

@csrf_exempt
def get_newspaperorders(request):
    temp = NewspaperOrder.objects.all()
    serializer = NewspaperOrderSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class NewspaperOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewspaperOrder.objects.all()
    serializer_class = NewspaperOrderSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
    

@csrf_exempt
def get_userprofiles(request):
    temp = UserProfile.objects.all()
    serializer = UserProfileSerializer(temp, many=True)
    return JsonResponse(serializer.data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
''''
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
'''