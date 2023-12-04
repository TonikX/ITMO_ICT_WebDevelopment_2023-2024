from rest_framework import generics, permissions, views, exceptions, viewsets
from rest_framework.response import Response
from projectFirst_app import serializers, models
from django.db import models as dj_models
from datetime import datetime, timedelta
from abc import abstractmethod


class CapsuleCreateView(generics.CreateAPIView):
    serializer_class = serializers.VaultCreateSerializer
    queryset = models.Vault.objects.all()


class CapsuleListView(generics.ListAPIView):
    queryset = models.Vault.objects.filter(eDate__lte=datetime.now())
    serializer_class = serializers.SimpleVaultSerializer


class CapsuleDetailView(generics.RetrieveAPIView):
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer


class CapsuleUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vault.objects.all()
    serializer_class = serializers.VaultSerializer


class CapsuleAccessListView(generics.ListAPIView):
    serializer_class = serializers.VaultAccessSerializer

    def get_queryset(self):
        vault_pk = self.kwargs.get('vault_pk', None)
        queryset = models.VaultAccess.objects.filter(vault_id=vault_pk)
        return queryset


class CapsuleAccessCreateView(generics.CreateAPIView):
    serializer_class = serializers.AccessCreateSerializer
    queryset = models.VaultAccess.objects.all()


class CapsuleFileListView(generics.ListAPIView):
    serializer_class = serializers.FileSerializer

    def get_queryset(self):
        vault_pk = self.kwargs.get('vault_pk', None)
        queryset = models.File.objects.filter(vault_id=vault_pk)
        return queryset


class CapsuleFileCreateView(generics.CreateAPIView):
    serializer_class = serializers.FileCreateSerializer
    queryset = models.File.objects.all()


class CapsuleCommentsView(generics.ListAPIView):
    serializer_class = serializers.CommentsSerializer

    def get_queryset(self):
        comment_pk = self.kwargs.get('comment_pk', None)
        vault_pk = self.kwargs.get('vault_pk', None)
        if(comment_pk == None):
            queryset = models.Comments.objects.filter(vault_id=vault_pk, mainComment=None)
        else:
            queryset = models.Comments.objects.filter(vault_id=vault_pk, id=comment_pk)
        return queryset


class CapsuleCommentCreateView(generics.CreateAPIView):
    serializer_class = serializers.CommentCreateSerializer
    queryset = models.Comments.objects.all()


class PeopleListView(generics.ListAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.SubPersonSerializer


class PersonDetailView(generics.RetrieveAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class PeopleFriendShipView(generics.CreateAPIView):
    queryset = models.FriendShip.objects.all()
    serializer_class = serializers.FriendShipCreateSerializer
