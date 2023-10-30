from .models import Tourist
from django.views.generic.edit import CreateView
from .forms import TouristCreationForm


class TouristCreateView(CreateView):
    model = Tourist
    form_class = TouristCreationForm
    success_url = "/tours"
    template_name = "tourist_form.html"
