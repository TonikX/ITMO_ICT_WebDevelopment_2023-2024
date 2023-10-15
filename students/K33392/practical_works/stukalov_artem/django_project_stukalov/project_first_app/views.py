from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Driver


def index(request):
    return render(request, "project_first_app/index.html")


def get_driver(request, driver_id):
    try:
        driver = get_object_or_404(Driver, pk=driver_id)
        pass
    except:
        raise Http404("Poll does not exist")

    return render(request, "project_first_app/get_driver.html", {"driver": driver})
