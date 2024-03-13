from collections import defaultdict

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from apps.homework.forms import SubmissionForm
from apps.homework.models import Subject, Submission, Homework
from apps.user.models import Student


class HomeView(TemplateView):
    template_name = 'homework/home.html'


class SubjectListView(ListView):
    model = Subject
    template_name = 'homework/subjects.html'
    context_object_name = 'subjects'


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'homework/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = self.get_object()
        context['teachers'] = subject.teachers.all()
        context['homeworks'] = subject.homeworks.all()
        return context


class SubmissionCreateView(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'homework/submission_form.html'

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        form.instance.homework = Homework.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('subject_list')  # TODO


class StudentSubmissionsView(TemplateView):
    template_name = 'homework/student_submissions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = get_object_or_404(Student, user=self.request.user)
        submissions = Submission.objects.filter(student=student).select_related('homework__subject').prefetch_related(
            'grade')

        grouped_submissions = defaultdict(list)
        for submission in submissions:
            grouped_submissions[submission.homework.subject.name].append(submission)

        context['grouped_submissions'] = dict(grouped_submissions)
        return context
