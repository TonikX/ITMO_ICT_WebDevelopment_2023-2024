from django.db import models


class Mountain(models.Model):
    name = models.CharField(max_length=100)
    height = models.PositiveIntegerField()
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Route(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Difficult', 'Difficult'),
        ('Expert', 'Expert'),
    ]
    
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE, related_name='routes')
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    length = models.PositiveIntegerField()
    peak_height = models.PositiveIntegerField()
    estimated_time = models.DurationField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} on {self.mountain.name}"
