from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Alpinist, Guide
from .permissions import CurrentUserOrAdmin
from .serializers import AlpinistSerializer, GuideSerializer
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
