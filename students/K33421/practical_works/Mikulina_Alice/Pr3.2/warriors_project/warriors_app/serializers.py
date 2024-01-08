from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):

  class Meta:
     model = Warrior
     fields = "__all__"


class WarriorCreateSerializer(serializers.ModelSerializer):
   
   class Meta:
     model = Warrior
     fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):

  class Meta:
     model = Profession
     fields = "__all__"


class ProfessionCreateSerializer(serializers.ModelSerializer):
   
   class Meta:
     model = Profession
     fields = "__all__"


class ProfessionDetailSerializer(serializers.ModelSerializer):
   
   class Meta:
     model = Profession
     fields = "__all__"