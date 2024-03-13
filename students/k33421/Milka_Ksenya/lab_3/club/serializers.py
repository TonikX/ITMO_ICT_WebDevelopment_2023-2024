from rest_framework import serializers

from .models import Climber, Climb, Club, Group, GroupMember, Mentor, Mountain, Route


class AlpinistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = ['id', 'user_id', 'date_of_birth', 'address', 'level', 'club']
        read_only_fields = ['id']


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id', 'user_id', 'certification', 'years_of_experience']
        read_only_fields = ['id']


class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = ['id', 'name', 'height', 'country', 'region']
        read_only_fields = ['id']


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'mountain_id', 'name', 'difficulty', 'length', 'peak_height', 'estimated_time', 'description']
        read_only_fields = ['id']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'country', 'city', 'contact_person', 'email', 'phone', 'website', 'created_at']
        read_only_fields = ['id']


class ClimbSerializer(serializers.ModelSerializer):
    route_id = serializers.PrimaryKeyRelatedField(
        queryset=Route.objects.all(), source='route', required=True, write_only=True
    )
    
    class Meta:
        model = Climb
        fields = ['id', 'route_id', 'start_date_planned', 'end_date_planned', 'start_date_actual', 'end_date_actual',
                  'guide_id', 'weather_conditions', 'group_outcome']
        read_only_fields = ['id']


class GroupSerializer(serializers.ModelSerializer):
    climb_id = serializers.PrimaryKeyRelatedField(
        queryset=Climb.objects.all(), source='climb', required=True, write_only=True
    )
    
    class Meta:
        model = Group
        fields = ['id', 'climb_id', 'member_count']
        read_only_fields = ['id']


class GroupMemberSerializer(serializers.ModelSerializer):
    group_id = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), source='group', required=True, write_only=True
    )
    
    class Meta:
        model = GroupMember
        fields = ['id', 'group_id', 'alpinist_id', 'outcome', 'incident']
        read_only_fields = ['id']
