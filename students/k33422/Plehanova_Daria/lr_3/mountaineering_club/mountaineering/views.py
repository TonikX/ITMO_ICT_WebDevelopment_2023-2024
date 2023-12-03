from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Alpinist, Guide
from .permissions import CurrentUserOrAdmin
from .serializers import AlpinistSerializer, GuideSerializer


class AlpinistViewSet(viewsets.ModelViewSet):
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
    search_fields = ['user__email', 'address']
    
    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        current_user = self.request.user
    
        if user_id and (current_user.is_staff or current_user.is_superuser):
            user = get_object_or_404(User, id=user_id)
        else:
            user = current_user
    
        serializer.save(user=user)


class GuideViewSet(viewsets.ModelViewSet):
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
    
    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        current_user = self.request.user
        
        if user_id and current_user.is_staff:
            user = get_object_or_404(User, id=user_id)
        else:
            user = current_user
        
        serializer.save(user=user)
