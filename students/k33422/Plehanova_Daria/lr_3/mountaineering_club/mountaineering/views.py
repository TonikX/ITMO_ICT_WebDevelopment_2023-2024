from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Alpinist, Climb, Club, Guide, Mountain, Route
from .permissions import CurrentUserOrAdmin, IsAdminOrReadOnly, IsGuideOrAdmin
from .serializers import AlpinistSerializer, ClimbSerializer, ClubSerializer, GuideSerializer, MountainSerializer, \
    RouteSerializer
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


class ClimbViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров climb.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения, изменение доступно только гидам и пользователям-администраторам
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
    permission_classes = [IsGuideOrAdmin]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['guide', 'route']
    search_fields = ['guide__user__email', 'guide__user__first_name', 'guide__user__last_name',
                     'route__name', 'route__mountain__name']
    
    def perform_create(self, serializer):
        guide_id = self.request.data.get('guide_id')
        current_user = self.request.user
        
        if guide_id and current_user.is_staff:
            guide = get_object_or_404(Guide, id=guide_id)
        else:
            guide = get_object_or_404(Guide, user=current_user)
        
        serializer.save(guide=guide)
