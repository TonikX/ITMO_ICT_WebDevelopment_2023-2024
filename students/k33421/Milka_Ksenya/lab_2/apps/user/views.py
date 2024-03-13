from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from apps.user.forms import UserRegisterForm, UserLoginForm
from apps.user.models import Student, Teacher, Roles


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        role = form.cleaned_data.get('role')

        if role == Roles.STUDENT:
            Student.objects.create(user=self.object)
        elif role == Roles.TEACHER:
            Teacher.objects.create(user=self.object)

        return response


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'user/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'user/information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_info'] = self.request.user
        return context
