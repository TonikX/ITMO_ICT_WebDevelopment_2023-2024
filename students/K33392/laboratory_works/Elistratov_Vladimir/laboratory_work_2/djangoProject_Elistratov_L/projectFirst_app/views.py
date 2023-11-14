from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


from .models import *

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView

from .forms import CreatePersonForm, LoginForm, BookForm, BookUpdForm

from datetime import timedelta

def CreatePersonView(request):
    if request.method == 'POST':
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/TytTour/main')
    else:
        form = CreatePersonForm()
    return render(request, 'registration.html', {'form': form})


def index(request):
    if(request.user.is_authenticated):
        tours = {}
        tours['dataset'] = Tour.objects.all()
        return render(request, "mainLogged.html", tours)
    else:
        userData = {}
        userData['username'] = request.user.username
        return render(request, "main.html", {'user': userData})


def LoginPerson(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is None:
                return HttpResponse('Invalid login')
            else:
                login(request, user=user)
                return redirect('/TytTour/main')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def LogoutPerson(request):
    if (request.user.is_authenticated):
        logout(request)
        #return HttpResponse('You have successfully logged out of your account')
    return redirect('/TytTour/main')


def booking(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if(form.is_valid()):
            treatyData = {}
            treatyData['startDate'] = (form.cleaned_data)['startDate']
            treatyData['pNum'] = (form.cleaned_data)['pNum']
            treatyData['userID'] = request.user
            treatyData['tourID'] = tour
            treatyData['endDate'] = timedelta(tour.duration) + treatyData['startDate']
            treatyData['cost'] = tour.cost * treatyData['pNum']
            treatyData['status'] = "w"
            ms = Treaty(
                startDate=treatyData['startDate'],
                customerID=treatyData['userID'],
                tourID=treatyData['tourID'],
                endDate=treatyData['endDate'],
                status=treatyData['status'],
                cost=treatyData['cost'],
                pNum=treatyData['pNum'],
            )
            ms.save()
            return redirect('/TytTour/profile/'+str(request.user.id))
        else:
            #print("NONE")
            pass
    else:
        form = BookForm()

    context = {}
    context['tour'] = tour
    context['form'] = form
    return render(request, 'book.html', {'data': context})


class userProfile(DetailView):
    model = Person
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(userProfile, self).get_context_data(**kwargs)
        context['booking'] = Treaty.objects.filter(customerID=self.request.user.id)
        return context


class userProfileUpdate(UpdateView):
    model = Person
    fields = ['fullName', 'birth_date', 'pSeries', 'pNumber',]
    template_name = "profileUpd.html"
    #success_url = "/TytTour/main"

    def get_context_data(self, **kwargs):
        context = super(userProfileUpdate, self).get_context_data(**kwargs)
        context['userInfo'] = self.request.user
        #self.success_url =
        return context

    def get_success_url(self):
        return ("/TytTour/profile/"+str(self.request.user.id))


class bookUpdate(UpdateView):
    model = Treaty
    fields = ['startDate', 'pNum', 'cost']
    template_name = "bookUpd.html"

    def get_success_url(self):
        return ("/TytTour/profile/"+str(self.request.user.id))

    def get_context_data(self, **kwargs):
        context = super(bookUpdate, self).get_context_data(**kwargs)
        context['tour'] = context['treaty'].tourID
        #print(context)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        request.POST = request.POST.copy()
        request.POST['cost'] = str(int(request.POST['pNum']) * self.object.tourID.cost)
        print(request.POST)
        return super(bookUpdate, self).post(request, **kwargs)


class bookDelete(DeleteView):
    model = Treaty
    template_name = "bookDel.html"

    def get_success_url(self):
        return ("/TytTour/profile/"+str(self.request.user.id))


class tourDetail(DetailView):
    model = Tour
    template_name = 'tourInfo.html'

    def get_context_data(self, **kwargs):
        context = super(tourDetail, self).get_context_data(**kwargs)
        comments = Comments.objects.filter(tourID=context['tour'])
        context['comments'] = comments
        return context


class createComment(CreateView):
    model = Comments
    template_name = 'comment.html'
    fields = ['commentText', 'grade']

    def get_success_url(self):
        bookId = self.kwargs.get('pk')
        url = ("/TytTour/tourinfo/"+str( (Treaty.objects.get(id=bookId)).tourID.id ) )
        #print(url)
        return url

    def form_valid(self, form):
        bookId = self.kwargs.get('pk')
        book = Treaty.objects.get(id=bookId)
        fields = form.save(commit=False)
        fields.authorID = book.customerID
        fields.tourID = book.tourID
        fields.tStartDate = book.startDate
        fields.tEndDate = book.endDate
        fields.save()
        return super().form_valid(form)