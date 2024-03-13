from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, serializers, viewsets

from .models import Climber, Climb, Club, Group, GroupMember, Mentor, Mountain, Route
from .permissions import CurrentUserOrAdminForGroupMember, CurrentUserOrAdminForProfiles, IsAdminOrReadOnly, \
    IsGuideOrAdminForClimb, \
    IsGuideOrAdminForGroup
from .serializers import AlpinistSerializer, ClimbSerializer, ClubSerializer, GroupMemberSerializer, GroupSerializer, \
    GuideSerializer, MountainSerializer, RouteSerializer
from .viewsets import BaseProfilesViewSet


class ClimberViewSet(BaseProfilesViewSet):
    queryset = Climber.objects.all()
    serializer_class = AlpinistSerializer
    permission_classes = [CurrentUserOrAdminForProfiles]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['level', 'club']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'address']


class MentorViewSet(BaseProfilesViewSet):
    queryset = Mentor.objects.all()
    serializer_class = GuideSerializer
    permission_classes = [CurrentUserOrAdminForProfiles]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['certification', 'years_of_experience']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']


class MountainViewSet(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country', 'region']
    search_fields = ['name']


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['difficulty']
    search_fields = ['name', 'mountain__name']


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country', 'city']
    search_fields = ['name', 'contact_person', 'email', 'phone']


class ClimbViewSet(viewsets.ModelViewSet):
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
            guide = get_object_or_404(Mentor, id=guide_id)
        else:
            guide = get_object_or_404(Mentor, user=current_user)
    
        serializer.save(guide=guide)


class GroupViewSet(viewsets.ModelViewSet):
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
            alpinist = get_object_or_404(Climber, id=alpinist_id)
        else:
            alpinist = get_object_or_404(Climber, user=current_user)
        
        serializer.save(alpinist=alpinist)
