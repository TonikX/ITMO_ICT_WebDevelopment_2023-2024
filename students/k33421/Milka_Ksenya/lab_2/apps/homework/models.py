from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from apps.user.models import Teacher, Student


class Subject(models.Model):
    teachers = models.ManyToManyField(Teacher, through='SubjectTeacher', related_name='subjects')
    name = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=9, validators=(
        RegexValidator(
            regex=r'^20\d{2}-20\d{2}$',
            message="Academic year must be in the format YYYY-YYYY, where Y is a digit."
        ),
    ))

    def __str__(self):
        return f"{self.name} - {self.academic_year}"


class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('subject', 'teacher')
        indexes = (
            models.Index(fields=('subject', 'teacher')),
        )

    def __str__(self):
        return f"{self.teacher} assigned to {self.subject} on {self.assigned_date}"


class Homework(models.Model):
    subject = models.ForeignKey(Subject, related_name='homeworks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    last_updated_date = models.DateTimeField(auto_now=True)

    @property
    def is_overdue(self):
        return timezone.now().date() > self.due_date

    def __str__(self):
        return f"{self.title} {self.issue_date} - {self.due_date}"


class Submission(models.Model):
    homework = models.ForeignKey(Homework, related_name='submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='submissions', on_delete=models.CASCADE)
    content = RichTextUploadingField()
    comments = models.TextField(blank=True)
    submission_date = models.DateField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = (
            models.Index(fields=('homework', 'student')),
        )
        unique_together = ('homework', 'student')

    @property
    def is_graded(self):
        return hasattr(self, 'grade')

    def __str__(self):
        return f"{self.homework.title} - {self.student}"


class Grade(models.Model):
    submission = models.OneToOneField(Submission, related_name='grade', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='grades', on_delete=models.CASCADE)
    value = models.IntegerField(validators=(MinValueValidator(1), MaxValueValidator(5)))
    comments = RichTextField()
    assigned_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.submission} - {self.value} by {self.teacher}"
