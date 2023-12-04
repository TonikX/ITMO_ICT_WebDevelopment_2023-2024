from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, serializers, viewsets

from .models import Alpinist, Climb, Club, Group, GroupMember, Guide, Mountain, Route
from .permissions import CurrentUserOrAdminForGroupMember, CurrentUserOrAdminForProfiles, IsAdminOrReadOnly, \
    IsGuideOrAdminForClimb, \
    IsGuideOrAdminForGroup
from .serializers import AlpinistSerializer, ClimbSerializer, ClubSerializer, GroupMemberSerializer, GroupSerializer, \
    GuideSerializer, MountainSerializer, RouteSerializer
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
    permission_classes = [CurrentUserOrAdminForProfiles]
    
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
    permission_classes = [CurrentUserOrAdminForProfiles]

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
    permission_classes = [IsGuideOrAdminForClimb]
    
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


class GroupViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров group.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения, изменение доступно только гидам и пользователям-администраторам
    * Поддерживает фильтрацию и поиск.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsGuideOrAdminForGroup]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['climb']
    search_fields = ['climb__route__name', 'climb__route__mountain__name', 'climb__guide__user__email',
                     'climb__guide__user__first_name', 'climb__guide__user__last_name']
    
    def perform_create(self, serializer):
        climb = serializer.validated_data['climb']
        
        member_count = self.request.data.get('member_count')
        current_user = self.request.user

        # Проверка, что гид climb совпадает с текущим пользователем
        if climb.guide.user != self.request.user and not self.request.user.is_staff:
            raise serializers.ValidationError({'climb': 'You are not a guide for this climb.'})

        # Если member_count предоставлен и пользователь является администратором
        if member_count and current_user.is_staff:
            serializer.save(member_count=member_count)
        else:
            serializer.save()


class GroupMemberViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для просмотра и редактирования экземпляров group_member.
    Предоставляет действия для list, create, retrieve, update, partial_update и destroy.
    
    * Требует аутентификации для чтения, изменение доступно только гидам и пользователям-администраторам
    * Поддерживает фильтрацию и поиск.
    """
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [CurrentUserOrAdminForGroupMember]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['group', 'alpinist']
    search_fields = ['incident', 'alpinist__user__email', 'alpinist__user__first_name', 'alpinist__user__last_name']
    
    def perform_create(self, serializer):
        alpinist_id = self.request.data.get('alpinist_id')
        current_user = self.request.user
        
        if alpinist_id and current_user.is_staff:
            alpinist = get_object_or_404(Alpinist, id=alpinist_id)
        else:
            alpinist = get_object_or_404(Alpinist, user=current_user)
        
        serializer.save(alpinist=alpinist)
