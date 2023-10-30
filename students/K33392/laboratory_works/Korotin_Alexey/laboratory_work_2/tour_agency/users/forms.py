from django.contrib.auth.forms import UserCreationForm
from .models import Tourist


class TouristCreationForm(UserCreationForm):
    class Meta:
        model = Tourist
        fields = ['username', 'first_name', 'last_name', 'passport']