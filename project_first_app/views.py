from datetime import datetime

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView

from project_first_app.models import AutoOwner, Auto


def auto_owner(request, owner_id):
    try:
        owner = AutoOwner.objects.get(pk=owner_id)
    except AutoOwner.DoesNotExist:
        raise Http404("Auto does not exist")
    return render(request, 'owner/detail.html', {'owner': owner})

def display_time(request):
    now = datetime.now()
    html = f"Time is {now}"
    return HttpResponse(html)

class AutoList(View):
    def get(self, request):
        autos = Auto.objects.all()
        context = {'autos': autos}
        return render(request, 'auto/list.html', context)

class AutoDetail(View):
    def get(self, request):
        context = {'auto': self.get_auto(request)}
        return render(request, 'auto/detail.html', context)

    def get_auto(self, request):
        auto_id = self.request.GET.get('id')

        if auto_id:
            try:
                auto_id = int(auto_id)
                auto = Auto.objects.filter(id=auto_id).first()
            except ValueError:
                auto = Auto.objects.none()
            return auto
        return Auto.objects.none()

class AutoRetrieveView(DetailView):
  model = Auto
class AutoUpdateView(UpdateView):
  model = Auto
  fields = ['brand', 'model', 'colour']
  success_url = '/auto/list/'


class AutoCreateView(CreateView):
  model = Auto
  fields = ['state_number', 'brand', 'model', 'colour']
  success_url = '/auto/list/'


class AutoDeleteView(DeleteView):
  model = Auto
  success_url = '/auto/list/'

class OwnerCreateView(CreateView):
  model = AutoOwner
  fields = ['first_name', 'last_name', 'birth_date']
  success_url = '/auto/list/'