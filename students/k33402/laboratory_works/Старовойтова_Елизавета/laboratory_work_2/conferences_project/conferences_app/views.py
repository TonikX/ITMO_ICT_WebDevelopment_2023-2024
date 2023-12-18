from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Conference, AuthorRegistration, Comment
from .forms import CommentForm, RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required

class ConferenceListView(ListView):
    model = Conference
    template_name = 'conference_list.html'
    context_object_name = 'conferences'

@login_required(login_url='/login/')
def user_confs_view(request, username):
    all_confs = Conference.objects.all()
    user_confs = []

    for conf in all_confs:
        if request.user in conf.members.all():
            user_confs.append(conf)
    return render(request, 'user_confs.html', {'user_confs': user_confs})
class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conference_detail.html'
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registrations'] = AuthorRegistration.objects.filter(conference=self.object)
        context['comments'] = Comment.objects.filter(conference=self.object)
        return context


class RegisterAuthorView(LoginRequiredMixin, View):
    template_name = 'registration_form.html'

    def get(self, request, *args, **kwargs):
        conference = get_object_or_404(Conference, pk=self.kwargs['pk'])

        is_registered = AuthorRegistration.objects.filter(user=request.user, conference=conference).exists()

        if is_registered:
            return redirect('conference_detail', pk=conference.pk)
        else:
            context = {'conference': conference}
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        conference = get_object_or_404(Conference, pk=self.kwargs['pk'])
        presentation_title = request.POST.get('presentation_title')  # Получаем значение из формы
        if not presentation_title:
            return render(request, self.template_name, {'conference': conference, 'error': 'Введите название доклада'})
        # Создаем объект AuthorRegistration с указанным названием доклада
        AuthorRegistration.objects.create(user=request.user, conference=conference, presentation_title=presentation_title)
        return redirect('conference_detail', pk=conference.pk)
class WriteCommentView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'write_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conference'] = get_object_or_404(Conference, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.conference = self.get_context_data()['conference']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.kwargs['pk']})


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()  # Создаем экземпляр формы для входа
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(self.request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('conference_list')
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('conference_list')

def logout_view(request):
    logout(request)
    return redirect('login')

class UpdateRegistrationView(LoginRequiredMixin, UpdateView):
    model = AuthorRegistration
    template_name = 'update_registration.html'
    fields = ['conference']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.object.conference.pk})


class DeleteRegistrationView(LoginRequiredMixin, DeleteView):
    model = AuthorRegistration
    template_name = 'delete_registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.object.conference.pk})



