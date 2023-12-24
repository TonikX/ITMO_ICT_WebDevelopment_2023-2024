from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import *


class MountainEasySerializer(serializers.ModelSerializer):

    class Meta:
        model = Mountain
        fields = "__all__"


class AlpinistEasySerializer(serializers.ModelSerializer):

    class Meta:
        model = Alpinist
        fields = ['id', 'first_name', 'last_name', 'experience_level']


class ClimbingEasySerializer(serializers.ModelSerializer):

    class Meta:
        model = Climbing
        fields = ['id', 'name', 'max_participants', 'cost', 'description', 'start_date_plan', 'finish_date_plan', 'level', 'mountain_id', 'club_id']


class ClubEasySerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ('id', 'name', 'state', 'city', 'contact_person', 'email', 'phone_number')


class ClubMembershipSerializer(serializers.ModelSerializer):
    club_id = serializers.StringRelatedField()
    alpinist_id = serializers.StringRelatedField()

    class Meta:
        model = ClubMembership
        fields = ('id', 'club_id', 'alpinist_id', 'date_from', 'admin_confirmation')#, 'admin_confirmation')

    '''def create(self, validated_data):

        membership = ClubMembership.objects.create(
                alpinist_id=self.context['request'].user,
                club_id=Club.objects.get(pk=1),
                date_from=validated_data.get('date_from'),
                #date_to=validated_data.get('date_to'),
                #admin_confirmation=validated_data.get('admin_confirmation', False)
            )
        return membership

    def update(self, instance, validated_data):
            instance.alpinist_id = validated_data.get('alpinist_id', instance.alpinist_id)
            instance.club_id = validated_data.get('club_id', instance.club_id)
            instance.date_from = validated_data.get('date_from', instance.date_from)
            instance.date_to = validated_data.get('date_to', instance.date_to)
            instance.admin_confirmation = validated_data.get('admin_confirmation', instance.admin_confirmation)
            instance.save()
            return instance

    def delete(self, instance):
            instance.delete()
            
            
            '''


class ClubMembershipCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClubMembership
        fields = ['id', 'club_id']

    def create(self, validated_data):
        club_id = validated_data.pop('club_id')
        club = get_object_or_404(Club, id=club_id)
        membership = ClubMembership.objects.create(club_id=club)
        return membership


class ParticipatingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participating
        fields = ['id']

    def create(self, validated_data):
        climbing_id = validated_data.pop('climbing_id')
        climbing = get_object_or_404(Participating, id=climbing_id)
        participating = Participating.objects.create(climbing_id=climbing)
        return participating


class ClimbingsSerializer(serializers.ModelSerializer):

    mountain_id = MountainEasySerializer()
    club_id = ClubEasySerializer()
    alpinists = AlpinistEasySerializer(many=True)

    class Meta:
        model = Climbing
        fields = ['id', 'name', 'description', 'start_date_plan', 'finish_date_plan', 'level', 'cost', 'max_participants', 'mountain_id', 'club_id', 'alpinists']


class ClubsSerializer(serializers.ModelSerializer):
    alpinists = AlpinistEasySerializer(many=True)#.objects.filter(admin_confirmation=True)

    class Meta:
        model = Club
        fields = ['id', 'name', 'state', 'city', 'contact_person', 'email', 'phone_number', 'alpinists']


class AlpinistsSerializer(serializers.ModelSerializer):
    clubs = ClubEasySerializer(many=True)
    climbings = ClimbingEasySerializer(many=True)

    class Meta:
        model = Alpinist
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'phone_number', 'email', 'address', 'experience_level', 'clubs', 'climbings']


class ParticipatingSerializer(serializers.ModelSerializer):
    #climbing_id = serializers.StringRelatedField()
    climbing_id = ClimbingEasySerializer()
    #alpinist_id = serializers.StringRelatedField()
    alpinist_id = AlpinistEasySerializer()

    class Meta:
        model = Participating
        fields = ['id', 'alpinist_id', 'climbing_id', 'succeed', 'admin_confirmation']#"__all__"

    '''def create(self, validated_data):
        content_object = validated_data.pop('climbing_id')
        content_object = get_object_or_404(Climbing, id=content_object)
        participating = Participating.objects.create(alpinist_id=self.context['request'].user, climbing_id=content_object)
        #participating = Participating.objects.create(
        #        alpinist_id=self.context['request'].user, #Alpinist.objects.get(pk=1),
        #        climbing_id=Climbing.objects.get(pk=validated_data.get('climbing_id')),
        #        )
        return participating'''




'''class ParticipatingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Climbing
        fields = "__all__"

    def create(self, validated_data):
        participating = Participating.objects.create(
                alpinist_id=self.context['request'].user, #Alpinist.objects.get(pk=1),
                climbing_id=Climbing.objects.get(pk=1),
                )
        return participating'''


class EmergencySerializer(serializers.ModelSerializer):
    participating_id = ParticipatingSerializer()

    class Meta:
        model = EmergensySituation
        fields = ['id', 'type', 'date', 'description', 'participating_id']


class ClimbingSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Climbing
        fields = ['id', 'name', 'description', 'start_date_plan', 'finish_date_plan', 'level']


class ClimbMountainSerializer(serializers.ModelSerializer):

    club_id = serializers.StringRelatedField()
    #alpinists = serializers.SlugRelatedField(many=True, read_only=True, slug_field='id')

    class Meta:
        model = Climbing
        fields = ['id', 'name', 'description', 'start_date_plan', 'finish_date_plan', 'level', 'club_id']


class ParticipatingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participating
        fields = ['succeed']

    def update(self, instance, validated_data):
        instance.succeed = validated_data.get('succeed', instance.succeed)
        instance.save()
        return instance


class ParticipatingDetailSerializer(serializers.ModelSerializer):
    climbing_id = ClimbingEasySerializer()
    #alpinist_id = AlpinistEasySerializer()

    class Meta:
        model = Participating
        fields = ['id', 'alpinist_id', 'climbing_id', 'succeed', 'admin_confirmation']  # "__all__"

#class ClubEasySerializerULR(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="user")

 #   class Meta:
  #      model = Club
   #     fields = ('url', 'id', 'name', 'state', 'city')
        #extra_kwargs = {
         #   'url': {'view_name': 'club-detail', 'lookup_field': 'id'}
        #}

