from os.path import join

from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tours_app.models import Traveler

__BASE_TEMPLATE_PATH = "traveler"


class TravelerModelForm(ModelForm):
    class Meta:
        model = Traveler
        fields = ["first_name", "last_name", "username", "password"]


def create_traveler_view(request: HttpRequest) -> HttpResponse:
    if (form := TravelerModelForm(request.POST or None)).is_valid():
        form.save()
    return render(request, join(__BASE_TEMPLATE_PATH, "create.html"), dict(form=form))
