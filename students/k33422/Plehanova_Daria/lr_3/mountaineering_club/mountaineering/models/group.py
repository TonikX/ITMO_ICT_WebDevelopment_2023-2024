from django.db import models

from .alpinist import Alpinist
from .climb import Climb


class Group(models.Model):
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE, related_name='groups')
    member_count = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Group for {self.climb}"


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    alpinist = models.ForeignKey(Alpinist, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=100)
    incident = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.alpinist.user.first_name} {self.alpinist.user.last_name} in {self.group}"
