### forms.py


Файл `forms.py` в Django используется для создания форм, которые обрабатывают ввод данных на стороне клиента (веб-странице)
Формы играют важную роль в обработке данных, валидации пользовательского ввода и представлении данных на веб-страницах.

В этой части кода я импортирую необходимые модули и классы Django для создания форм. Тут будут использоваться классы `ModelForm`, предоставляемые Django, чтобы автоматически создавать формы на основе моделей.

```
from django import forms
from .models import Presentation, Registration, Review, Author
```

В этой части кода создается форма `AuthorForm`. Эта форма связана с моделью `Author`, что означает, что она будет автоматически создана на основе полей этой модели. `fields` определяет, какие поля из модели включаются в форму. `labels` используется для определения пользовательских меток для полей формы.

```
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['username', 'password', 'first_name', 'last_name', 'occupation', 'is_admin']
        labels = {
            'username': 'username',
            'password': 'password',
            'first_name': 'name',
            'last_name': 'surname',
            'occupation': 'occupation',
            'is_admin': 'access status',
        }
```

Здесь создается форма `PresentationForm` для модели `Presentation`. Аналогично, указываю, какие поля из модели включаются в форму, и определяю пользовательские метки для полей.

```
class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['conference', 'author', 'title', 'approved_pres']
        labels = {
            'conference': 'conference',
            'author': 'assigned authors',
            'title': 'title',
            'approved_pres': 'approval status',
        }
```

В этой части создается форма `RegistrationForm` для модели `Registration`. Аналогично предыдущим формам, указываю, какие поля включаются и определяю пользовательские метки для полей.

```
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['author', 'conference', 'title', 'approved_reg']
        labels = {
            'author': 'conference',
            'conference': 'assigned authors',
            'title': 'title',
            'approved_reg': 'approval status',
        }
```

Здесь создается форма `ReviewForm` для модели `Review`. Отличие в том, что тут я использую `exclude` для исключения поля `comment_date` из формы.

```
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['comment_date']
        fields = ['conference', 'author', 'text', 'rating']
        labels = {
            'conference': 'conference',
            'author': 'author',
            'text': 'text',
            'rating': 'rating',
        }
```