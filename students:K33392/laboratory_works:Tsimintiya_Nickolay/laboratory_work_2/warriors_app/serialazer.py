from rest_framework import serializers
from .models import Warrior


class WarriorSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"
