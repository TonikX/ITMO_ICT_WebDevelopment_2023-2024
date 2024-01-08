from django.shortcuts import render
from .models import CarOwner, Car
from .forms import NewCar, NewOwner, EditCar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import Http404
from django.urls import reverse_lazy

class HomeView(ListView):
    model = CarOwner
    template_name = 'home.html'
    
class OwnerView(ListView):
    model = CarOwner
    template_name = 'owner.html'
    context_object_name = 'owner'
    
class DetailOwnerView(DetailView):
    model = CarOwner
    template_name = 'detail_owner.html'
    context_object_name = 'owner'
    
class CarView(ListView):
    model = Car
    template_name = 'car.html'
    context_object_name = 'car'
    
class DetailCarView(DetailView):
    model = Car
    template_name = 'detail_car.html'
    context_object_name = 'car'
    
class CreateCar(CreateView):
    model = Car
    form_class = NewCar
    template_name = 'new_car.html'
    success_url = reverse_lazy('car')

      
class EditCar(UpdateView):
    model = Car
    form_class = EditCar
    template_name = 'edit_car.html'
    success_url = reverse_lazy('car')

class DeleteCar(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = reverse_lazy('car')
    
class CreateOwner(CreateView):
    model = CarOwner
    form_class = NewOwner
    template_name = 'new_owner.html'
    success_url = reverse_lazy('owner')
  

