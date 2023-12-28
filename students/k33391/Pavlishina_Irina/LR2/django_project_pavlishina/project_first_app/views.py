from django.http import Http404
from django.shortcuts import render, redirect
from project_first_app.models import CarOwner, Car
from .forms import CarOwnerCreateForm, CarUpdateForm, CarCreateForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView


def owner(request, pk):
    try:
        founded_owner = CarOwner.objects.get(pk=pk)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': founded_owner})


###################################################3

def owners(request):
    visual = {"owners": CarOwner.objects.all()}
    return render(request, 'owners.html', visual)


def create_owner(request):
    match request.method:
        case "POST":
            form = CarOwnerCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("owners")
        case "GET":
            form = CarOwnerCreateForm()
            return render(
                request, "create_owner.html", {"form": form}
            )
        case _:
            return Http404(f"Method {request.method} not supported")

##################


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"


class CarListView(ListView):
    model = Car
    template_name = "car_list.html"
    context_object_name = "cars"


class CarCreateView(CreateView):
    model = Car
    template_name = "car_create.html"
    form_class = CarCreateForm
    success_url = "/cars"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    success_url = "/cars"
    template_name = "car_update.html"


class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/cars"