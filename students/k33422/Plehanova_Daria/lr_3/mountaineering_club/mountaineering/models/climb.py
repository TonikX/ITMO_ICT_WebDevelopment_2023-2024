from django.db import models

from .guide import Guide
from .mountain import Route


class Climb(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='climbs')
    start_date_planned = models.DateTimeField()
    end_date_planned = models.DateTimeField()
    start_date_actual = models.DateTimeField(null=True, blank=True)
    end_date_actual = models.DateTimeField(null=True, blank=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='climbs')
    weather_conditions = models.TextField(blank=True)
    group_outcome = models.TextField()
    
    def __str__(self):
        return f"{self.route} with {self.guide} ({self.start_date_planned})"
