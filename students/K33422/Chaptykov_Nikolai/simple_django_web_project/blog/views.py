from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from blog.models import Person, OwnerShip, ExampleModel, Publisher, Book, Car
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from blog.forms import ExampleForm, PersonForm, UserForm, ProfileForm
from django.db import transaction


def detail(request, owner_id):
    try:
        obj = Person.objects.get(pk=owner_id)
        name = obj.first_name
        surname = obj.last_name
        birthday = obj.birthdate
    except Person.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'detail.html', {'first_name': name, 'last_name': surname, 'birthday': birthday})

def getDate(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)

def listView(request):
    context = {}
    context["dataset"] = ExampleModel.objects.all()
    return render(request, 'list_view.html', context)


class ExampleList(ListView):
    model = ExampleModel
    template_name = 'cvb_list_view.html'


class PublisherRetrieveView(DetailView):
    model = Publisher
    template_name = 'publisher_detail.html'


class BookListView(ListView):
    model = Book
    queryset = model.objects.all()
    template_name = 'book_list.html'

    def get_queryset(self):
        publisher = self.request.GET.get('publisher')
        if publisher:
            try:
                publisher = int(publisher)
                queryset = self.queryset.filter(publisher=publisher)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = 'car_list.html'


def PersonListView(request):
    context = {}
    context["dataset"] = Person.objects.all()
    return render(request, 'person_list.html', context)
    
def create_view(request):
    context ={}
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['first_name', 'last_name', 'birthdate']
    success_url = '/publisher/list/'
    template_name = 'publisher_form.html'


class ExampleCreate(CreateView):
    model = ExampleModel
    template_name = 'cvb_create_view.html'
    fields = ['title', 'description']


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'cvb_create_view.html'
    fields = ['title', 'description']


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = '/publisher/list/'
    template_name = 'publisher_confirm_delete.html'


def PostPerson(request):
    context = {}
    form = PersonForm(request.POST or None) 
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarCreate(CreateView):
    model = Car
    template_name = 'cvb_create_view.html'
    success_url = '/cars'
    fields = ['plate_number', 'company_produced', 'model', 'color']


class CarUpdate(UpdateView):
    model = Car
    fields = ['plate_number', 'company_produced', 'model', 'color']
    success_url = '/cars'
    template_name = 'car_form.html'


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'
    template_name = 'car_confirm_delete.html'


class CarDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'


from django.contrib.auth.decorators import login_required


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })