from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class UniversalListView(generics.ListAPIView):
    model = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = self.model.objects.all()


class UniversalRetrieveView(generics.RetrieveAPIView):
    model = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = self.model.objects.all()


class UniversalCreateView(generics.CreateAPIView):
    model = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = self.model.objects.all()


class UniversalUpdateView(generics.UpdateAPIView):
    model = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = self.model.objects.all()


class UniversalDeleteView(generics.DestroyAPIView):
    model = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queryset = self.model.objects.all()


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
