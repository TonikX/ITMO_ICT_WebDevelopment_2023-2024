from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Club(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Climber(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alpinist_profile')
    date_of_birth = models.DateField()
    address = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Beginner')
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True, related_name='alpinists')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


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


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guide_profile')
    certification = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Climb(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='climbs')
    start_date_planned = models.DateTimeField()
    end_date_planned = models.DateTimeField()
    start_date_actual = models.DateTimeField(null=True, blank=True)
    end_date_actual = models.DateTimeField(null=True, blank=True)
    guide = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='climbs')
    weather_conditions = models.TextField(blank=True)
    group_outcome = models.TextField()

    def __str__(self):
        return f"{self.route} with {self.guide} ({self.start_date_planned})"


class Group(models.Model):
    climb = models.ForeignKey(Climb, on_delete=models.CASCADE, related_name='groups')
    member_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Group for {self.climb}"


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    alpinist = models.ForeignKey(Climber, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=100, null=True, blank=True)
    incident = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.alpinist.user.first_name} {self.alpinist.user.last_name} in {self.group}"
