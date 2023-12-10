# Описание urls.py и форм

Тут я приведу код к urls.py и немного расскажу о формах.

### Urls

urls.py у меня встречается дважды - в приложениях `Users` и `Journal`. Они тесно связаны с представлениями, так что оставлю эту часть без объяснений.

``` py title="users/urls.py"
from django.urls import path, include
from .views import UserRegister, UserEditing
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'register'),
    path('edit_profile/', UserEditing.as_view(), name = 'edit'),
    path('password/', auth_views.PasswordChangeView.as_view()),
    
]

```

``` py title="journal/urls.py"
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import HomePage, HomeworkPage, AddHomework, EditHomework, DeleteHomework, SubmitHomework, GradeHomework, StudentGrades, GradeStudentHomework
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', login_required(HomePage.as_view()), name='home'),
    path('homework/<int:pk>', login_required(HomeworkPage.as_view()), name='homework-page'),
    path('add_homework/', login_required(AddHomework.as_view()), name='new-homework'),
    path('homework/edit/<int:pk>', login_required(EditHomework.as_view()), name='edit-homework'),
    path('homework/<int:pk>/delete/', login_required(DeleteHomework.as_view()), name='delete-homework'),
    path('homework/<int:pk>/submit/', login_required(SubmitHomework.as_view()), name='submit-homework'),
    path('grade_homework/', login_required(GradeHomework.as_view()), name='grade-homework'),
    path('student_grades/<int:student_id>/', login_required(StudentGrades.as_view()), name='student-grades'),
    path('student_homework/<int:student_id>/<int:submission_id>/', login_required(GradeStudentHomework.as_view()), name='grade-student-homework'),

]

```

### Forms

``` py title="users/forms.py"
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditForm(UserChangeForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

```

Формы для авторизации стандартные. Единственное изменение - это невозможность со стороны пользователя редактировать имя и фамилию. Их может поменять только админ.

``` py title="journal/forms.py"
from django import forms
from .models import Profile, Homework, SubmittedHomework
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone 

class PostHomework(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('subject', 'body', 'end_date', 'student_class', 'subject')

        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'end_date': DateTimePickerInput(
                attrs={'class': 'form-control'},
                options={
                    'format': 'DD-MM-YYYY HH:mm',
                    'showTodayButton': True,
                    'minDate': timezone.now().strftime('%Y-%m-%d %H:%M'),
                }
            ),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super().__init__(*args, **kwargs)
        student_classes = Profile.objects.filter(role='student').values_list('student_class', flat=True).distinct()
        class_choices = [(cls, cls) for cls in student_classes]
        class_choices.insert(0, ('', 'Choose a class'))
        self.fields['student_class'].widget.choices = class_choices
        if user and user.profile.role == 'teacher':
            allowed_subjects = user.profile.subjects.all().distinct()
            allowed_subjects = [(cls.name, cls.name) for cls in allowed_subjects]
            allowed_subjects.insert(0, ('', 'Choose a subject'))
            self.fields['subject'].widget.choices = allowed_subjects

class EditHomework(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('body', 'end_date', 'student_class')

        widgets = {
                'body': forms.Textarea(attrs={'class': 'form-control'}),
                'end_date': DateTimePickerInput(
                    attrs={'class': 'form-control'},
                    options={
                        'format': 'DD-MM-YYYY HH:mm',
                        'showTodayButton': True,
                        'minDate': timezone.now().strftime('%Y-%m-%d %H:%M'),
                    }
                ),
                'student_class': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        student_classes = Profile.objects.filter(role='student').values_list('student_class', flat=True).distinct()
        class_choices = [(cls, cls) for cls in student_classes]
        self.fields['student_class'].widget.choices = class_choices

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = SubmittedHomework
        fields = ('homework_body',)
        widgets = {
            'homework_body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

```

Формы `PostHomework` и `EditHomework` отвечают за создание и редактирования домашнего задания учителем. Есть несколько ограничений - нельзя выставить дату меньше текущей, есть ограниченный выбор из существующих классов и доступных предметов.

Форма `SubmissionForm` принимает домашнее задания ученика.