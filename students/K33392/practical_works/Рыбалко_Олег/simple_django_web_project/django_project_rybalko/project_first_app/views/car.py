from os.path import join

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from project_first_app.models import Car


class CarDetailView(DetailView):
    model = Car
    template_name = join("car", "detail.html")


class CarListView(ListView):
    model = Car
    template_name = join("car", "all.html")


class CarUpdateView(UpdateView):
    model = Car
    fields = ["number", "model", "color"]
    success_url = "/cars"
    template_name = join("car", "update.html")


class CarCreateView(CreateView):
    model = Car
    fields = ["number", "model", "color"]
    success_url = "/cars"
    template_name = join("car", "create.html")


class CarDeleteView(DeleteView):
    model = Car
    fields = ["number", "model", "color"]
    success_url = "/cars"
    template_name = join("car", "delete.html")
