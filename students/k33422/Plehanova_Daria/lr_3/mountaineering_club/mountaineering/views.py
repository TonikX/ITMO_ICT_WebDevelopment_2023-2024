from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Alpinist, Guide, Mountain, Route, Club
from .permissions import CurrentUserOrAdmin, IsAdminOrReadOnly
from .serializers import AlpinistSerializer, GuideSerializer, MountainSerializer, RouteSerializer, ClubSerializer
from .viewsets import BaseProfilesViewSet


class AlpinistViewSet(BaseProfilesViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров alpinist.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения и создания, обновлять и удалять профили могут
    только их владельцы или пользователи-администраторы
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Alpinist.objects.all()
    serializer_class = AlpinistSerializer
    permission_classes = [CurrentUserOrAdmin]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['level', 'club']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'address']


class GuideViewSet(BaseProfilesViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров guide.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения и создания, обновлять и удалять профили могут
    только их владельцы или пользователи-администраторы
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    permission_classes = [CurrentUserOrAdmin]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['certification', 'years_of_experience']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']


class MountainViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров mountain.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения, изменение доступно только пользователям-администраторам
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country', 'region']
    search_fields = ['name']


class RouteViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров route.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения, изменение доступно только пользователям-администраторам
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['difficulty']
    search_fields = ['name', 'mountain__name']


class ClubViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров club.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения, изменение доступно только пользователям-администраторам
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country', 'city']
    search_fields = ['name', 'contact_person', 'email', 'phone']
