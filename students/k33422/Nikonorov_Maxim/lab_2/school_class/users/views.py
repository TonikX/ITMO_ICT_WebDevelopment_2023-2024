from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditForm

class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditing(generic.UpdateView):
    form_class = EditForm
    template_name = 'registration/edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    



    