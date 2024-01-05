from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseBadRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *


def owner_detail(request, owner_id):
	try:
		owner = Owner.objects.get(pk=owner_id)
	except Owner.DoesNotExist:
		raise Http404("Owner does not exist")
	return render(request, 'owner_detail.html', {'owner': owner})


def owner_list(request):
	owners = Owner.objects.all()
	return render(request, 'owner_list.html', {'owners': owners})


class CarList(ListView):
	model = Car
	template_name = 'car_list.html'


class CarDetail(DetailView):
	model = Car
	template_name = 'car_detail.html'


def owner_create(request):
	data = request.POST or None
	if not data:
		return render(request, 'owner_create.html', {'form': OwnerForm()})
	form = OwnerForm(data)
	if not form.is_valid():
		return HttpResponseBadRequest(form.errors)
	form.save()
	return redirect('owner_list')


class CarCreate(CreateView):
	model = Car
	fields = '__all__'
	template_name = 'car_create.html'
	success_url = reverse_lazy('car_list')


class CarUpdate(UpdateView):
	model = Car
	fields = '__all__'
	template_name = 'car_update.html'

	def post(self, request, *args, **kwargs):
		pk = kwargs.get('pk')
		if not Car.objects.filter(pk=pk).exists():
			return Http404('Car does not exist')
		car = Car.objects.get(pk=pk)
		data = request.POST
		form = CarForm(data=data, instance=car)
		if not form.is_valid():
			return HttpResponseBadRequest(str(form.errors))
		form.save()
		return redirect('car_detail', pk=pk)


class CarDelete(DeleteView):
	model = Car
	template_name = 'car_delete.html'
	success_url = reverse_lazy('car_list')
