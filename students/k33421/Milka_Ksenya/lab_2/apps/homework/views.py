from collections import defaultdict

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from apps.homework.forms import SubmissionForm, GradeForm
from apps.homework.models import Subject, Submission, Homework, Grade
from apps.user.models import Student, Teacher


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


class TeacherHomeworkListView(TemplateView):
    template_name = 'homework/homework_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.request.user.teacher
        homeworks = Homework.objects.filter(subject__teachers=teacher).select_related('subject').order_by('subject')

        grouped_homeworks = defaultdict(list)
        for homework in homeworks:
            grouped_homeworks[homework.subject.name].append(homework)

        context['grouped_homeworks'] = dict(grouped_homeworks)
        return context


class TeacherHomeworkDetailView(DetailView):
    model = Homework
    template_name = 'homework/homework_detail.html'
    context_object_name = 'homework'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submissions'] = self.object.submissions.all().select_related('student')
        return context


class GradeSubmissionView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'homework/grade_submission.html'

    def get_initial(self):
        submission_pk = self.kwargs.get('pk')
        submission = get_object_or_404(Submission, pk=submission_pk)
        teacher_user = self.request.user
        teacher_profile = get_object_or_404(Teacher, user=teacher_user)
        initial = super().get_initial()
        initial['submission'] = submission
        initial['teacher'] = teacher_profile
        return initial

    def form_valid(self, form):
        submission_pk = self.kwargs.get('pk')
        submission = get_object_or_404(Submission, pk=submission_pk)
        form.instance.submission = submission

        teacher_user = self.request.user
        teacher_profile = get_object_or_404(Teacher, user=teacher_user)
        form.instance.teacher = teacher_profile

        return super().form_valid(form)

    def get_success_url(self):
        submission_pk = self.kwargs.get('pk')
        submission = get_object_or_404(Submission, pk=submission_pk)
        return reverse_lazy('teacher_homework_detail', kwargs={'pk': submission.homework.pk})
