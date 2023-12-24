from datetime import datetime
from urllib import request

from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters.rest_framework
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from rest_framework.filters import OrderingFilter
from .serializers import *
from .filters import *


class AlpinistsAPIView(ListAPIView):
    queryset = Alpinist.objects.all()
    serializer_class = AlpinistsSerializer
    permission_classes = (IsAuthenticated, )


class ClimbingsListView(ListAPIView):
    queryset = Climbing.objects.all()
    serializer_class = ClimbingEasySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['start_date_plan', 'level']
    filterset_class = ClimbingsFilter


class ClimbingsDetailView(RetrieveAPIView):
    queryset = Climbing
    serializer_class = ClimbingsSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Climbing.objects.filter(id=self.kwargs['pk'])


class MountainsListView(ListAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainEasySerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = MountainsFilter


class MountainsDetailView(RetrieveAPIView):
    queryset = Mountain
    serializer_class = MountainEasySerializer

    def get_queryset(self):
        return Mountain.objects.filter(id=self.kwargs['pk'])


class ParticipationAPIView(viewsets.ModelViewSet):
    queryset = Participating.objects.all()
    serializer_class = ParticipatingSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('climbing_id', 'admin_confirmation')# 'alpinist_id')
    permission_classes = (IsAuthenticated, )


class ParticipatingDetailView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_pk')
        part = self.get_object()
        if request.user.id == user_id and part.user.id == user_id:
            part = get_object_or_404(Participating, pk=self.kwargs['pk'])
            serializer = ParticipatingDetailSerializer(part)
            return Response(serializer.data)
        else:
            raise PermissionDenied(detail='You are unauthorized')


class ParticipatingCreateView(generics.CreateAPIView):
    serializer_class = ParticipatingCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        if request.user.id == user_id:
            user = request.user
            #climbing_id = request.data.get('climbing_id')
            climbing = get_object_or_404(Climbing, id=self.kwargs.get('pk'))#climbing_id)
            participating = Participating.objects.filter(alpinist_id=user, climbing_id=climbing).first()
            if participating:
                return Response({'detail': 'Object already exists in favorites'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                Participating.objects.create(alpinist_id=user, climbing_id=climbing)
            return Response({'detail': 'Favorite object created successfully'}, status=status.HTTP_201_CREATED)
        else:
            raise PermissionDenied(detail='Unauthorized/Wrong authorization')


class ParticipatingDeleteView(generics.DestroyAPIView):
    queryset = Participating
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_pk')
        part = self.get_object()
        if request.user.id == user_id and part.user.id == user_id:
            self.perform_destroy(part)
            return Response({'detail': 'Your participation successfully deleted'}, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied(detail='You are unauthorized')


class ParticipatingUpdateView(generics.UpdateAPIView):
    queryset = Participating.objects.all()
    serializer_class = ParticipatingUpdateSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "your participating updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class ClubMemberViewSet(viewsets.ModelViewSet):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('club_id', )
    permission_classes = (IsAuthenticated, )


class ClubMembershipCreateView(generics.CreateAPIView):
    serializer_class = ClubMembershipCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if request.user.id == user_id:
            user = request.user
            club_id = request.data.get('club_id')
            club = get_object_or_404(Club, id=club_id)
            club_membership = ClubMembership.objects.filter(alpinist_id=user, club_id=club).first()
            if club_membership:
                return Response({'detail': 'Object already exists in favorites'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                ClubMembership.objects.create(alpinist_id=user, club_id=club)
            return Response({'detail': 'Favorite object created successfully'}, status=status.HTTP_201_CREATED)
        else:
            raise PermissionDenied(detail='Unauthorized')


class ClubMembershipDeleteView(generics.DestroyAPIView):
    queryset = ClubMembership
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_pk')
        part = self.get_object()
        if request.user.id == user_id and part.user.id == user_id:
            self.perform_destroy(part)
            return Response({'detail': 'Your club membership successfully deleted'}, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied(detail='You are unauthorized')


class ClubsListView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubEasySerializer


class ClubDetailView(RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubsSerializer

    def get_queryset(self):
        return Club.objects.filter(id=self.kwargs['pk'])


class EmergencyListView(ListAPIView):
    queryset = EmergensySituation.objects.all()
    serializer_class = EmergencySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('participating_id', 'type')
    permission_classes = (IsAuthenticated, )



    '''def delete(self, request, *args, **kwargs):
        part = get_object_or_404(Participating, pk=self.kwargs['pk'])
        part.delete()
        return Response({'detail': 'Your participation successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        part = get_object_or_404(Participating, pk=self.kwargs['pk'])
        serializer = ParticipatingDetailSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''

#class ClubDetailAPIView(APIView):
 #   def get(self, request, pk):
  #      club = Club.objects.get(pk=pk)
   #     serializer = ClubEasySerializer(club, context={'request': request})
    #    return Response(serializer.data)


#class MountainListView(ListAPIView):
 #   queryset = Mountain.objects.all()
  #  serializer_class = MountainSerializer1

   # def get_queryset(self):
    #    return Mountain.objects.filter(climbing__start_date_plan__gte=datetime.now().date()).distinct()


#class ClubsView(APIView):

 #   def get(self, request, post_id):
  #      clubs = Club.objects.all()
   #     serializer = ClubsSerializer#(clubs, many=True, context={'request': request})
    #    return Response(serializer.data)


#class MountainListView(ListAPIView):
 #   queryset = Mountain.objects.all()
 #   serializer_class = MountainSerializer1

  #  def get_queryset(self):
   #     return Mountain.objects.filter(climbing__start_date_plan__gte=datetime.now().date()).distinct()


'''class ClubMembershipView(APIView):
    def post(self, request):
        serializer = ParticipatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            membership = ClubMembership.objects.get(pk=pk)
        except ClubMembership.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''class ParticipatingForClimbingCreateView(APIView):
    def get_object(self, pk):
        try:
            return Climbing.objects.get(pk=pk)
        except Climbing.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        a = self.get_object(pk)
        serializer = ClimbingEasySerializer(a)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        a = self.get_object(pk)
        serializer = ParticipatingDetailSerializer(data=request.data)
        if serializer.is_valid():
            b = serializer.save()
            #a.b_set.add(b)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
#class ClimbMountainView(RetrieveAPIView):
 #   queryset = Climbing.objects.all()
  #  serializer_class = ClimbMountainSerializer

   # def get_queryset(self):
     #   return Climbing.objects.filter(mountain_id=self.kwargs['pk'])




