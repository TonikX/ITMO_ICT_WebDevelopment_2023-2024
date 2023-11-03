from os.path import join

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from project_first_app.models import Car


class CarDetailView(DetailView):
    model = Car
    template_name = join("car", "detail.html")


class CarListView(ListView):
    model = Car
    template_name = join("car", "all.html")
