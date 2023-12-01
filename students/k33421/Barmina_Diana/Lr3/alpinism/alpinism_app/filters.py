from rest_framework import generics
from django_filters import rest_framework as filters
from .models import *


class ClimbingsFilter(filters.FilterSet):
    min_cost = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    max_cost = filters.NumberFilter(field_name="cost", lookup_expr='lte')
    min_date = filters.DateFilter(field_name="start_date_plan", lookup_expr='gte')
    max_date = filters.DateFilter(field_name="finish_date_plan", lookup_expr='lte')

    class Meta:
        model = Climbing
        fields = ['club_id', 'mountain_id', 'level']


class MountainsFilter(filters.FilterSet):
    min_height = filters.NumberFilter(field_name='hight', lookup_expr='gte')
    max_height = filters.NumberFilter(field_name='hight', lookup_expr='lte')

    class Meta:
        model = Mountain
        fields = ['name', 'state']

