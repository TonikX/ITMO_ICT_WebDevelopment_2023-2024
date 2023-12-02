from rest_framework import serializers
from .models import Crew, CrewMember, AirlineCompany, Airplane, Route, Flight

class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = '__all__'

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = '__all__'

class CrewSerializer(serializers.ModelSerializer):
    members = CrewMemberSerializer(many=True, read_only=True)

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    airplanes = AirplaneSerializer(many=True)
    crew = CrewSerializer(many=True)

    class Meta:
        model = Flight
        fields = '__all__'

    def create(self, validated_data):
        airplanes_data = validated_data.pop('airplanes', [])
        crew_data = validated_data.pop('crew', [])

        flight = Flight.objects.create(**validated_data)

        for airplane_data in airplanes_data:
            Airplane.objects.create(flight=flight, **airplane_data)

        for crew_member_data in crew_data:
            CrewMember.objects.create(flight=flight, **crew_member_data)

        return flight
