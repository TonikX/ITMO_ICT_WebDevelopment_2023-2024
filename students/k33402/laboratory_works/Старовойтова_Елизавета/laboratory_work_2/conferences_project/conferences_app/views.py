from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
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
from django.contrib.auth.mixins import LoginRequiredMixin

class ConferenceListView(ListView):
    model = Conference
    template_name = 'conference_list.html'
    context_object_name = 'conferences'

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
    def get(self, request, *args, **kwargs):
        conference = get_object_or_404(Conference, pk=self.kwargs['pk'])

        is_registered = AuthorRegistration.objects.filter(user=request.user, conference=conference).exists()

        if is_registered:

            return redirect('conference_detail', pk=conference.pk)
        else:
            # Если пользователь не зарегистрирован, отображаем форму для регистрации.
            form = RegistrationForm()  # Используйте свою форму регистрации
            context = {'form': form, 'conference': conference}
            return render(request, 'registration_form.html', context)


    def post(self, request, *args, **kwargs):
        conference = get_object_or_404(Conference, pk=self.kwargs['pk'])
        AuthorRegistration.objects.create(user=request.user, conference=conference)
        return redirect('conference_detail', pk=conference.pk)
class WriteCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'write_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получение объекта Conference по его id (pk)
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
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # Указываем URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()  # Создаем экземпляр формы для входа
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request, request.POST)
        if form.is_valid():
            return redirect('conference_list')

class UpdateRegistrationView(LoginRequiredMixin, UpdateView):
    model = AuthorRegistration
    template_name = 'update_registration.html'
    fields = ['conference']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = self.object  # Добавляем объект регистрации в контекст
        return context

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.object.conference.pk})

class DeleteRegistrationView(LoginRequiredMixin, DeleteView):
    model = AuthorRegistration
    template_name = 'delete_registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = self.object  # Добавляем объект регистрации в контекст
        return context

    def get_success_url(self):
        return reverse_lazy('conference_detail', kwargs={'pk': self.object.conference.pk})


