### views.py


Файл `views.py` в Django - это место, где определяются функции (или классы) представлений, которые обрабатывают HTTP-запросы и возвращают HTTP-ответы. 
Он играет ключевую роль в определении того, как данные будут представлены и как пользователи будут взаимодействовать с приложением.

Ниже импортирую все необходимые модули `Django`, а также модели из файлов проекта.
```
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Author, Conference, Registration, Presentation, Review
from .forms import AuthorForm, RegistrationForm, PresentationForm, ReviewForm
```

Функция представления (ниже) отвечает за отображение домашней страницы приложения. Когда пользователь заходит на главную страницу, эта функция возвращает HTML-шаблон `home.html`. 
В моем случае, я использую его для создания простой домашней страницы без дополнительной информации.
```
def home(request):
    return render(request, 'home.html', {})
```

В этой функции я получаю все записи из модели `Author` с помощью `Author.objects.all()` и передаю их в шаблон `authors.html`.
```
def all_authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})
```

Эта функция отвечает за отображение деталей конкретного автора. 
Я использую `get_object_or_404`, чтобы получить объект `Author` с определенным идентификатором `author_id` или выдать ошибку `404`, если объект не найден.
```
def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})
```    

Этот класс представления `Django` наследуется от `CreateView` и предоставляет встроенную логику для создания новых авторов. Я указываю модель `Author` и форму `AuthorForm`, которую нужно использовать. 
Также я указываю, куда перенаправить пользователя после успешного создания автора.
```
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = '/'
```

Аналогично предыдущему классу, этот класс наследуется от класса `UpdateView`. 
Я указываю модель, форму и шаблон, который будет использоваться для редактирования.
```
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'edit_author.html'
    success_url = '/'
```

В этой функции я получаю все записи из модели `Registration` и передаю их в шаблон `registrations.html`. 
Таким образом, создается страница со списком всех регистраций.
```
def all_registrations(request):
    registrations_list = Registration.objects.all()
    return render(request, 'registrations.html', {'registrations': registrations_list})
```

Далее я использую почти одинаковые конструкции с теми, что представлены выше, для того чтобы получать информацию о регистрациях, выступлениях, конференция и обзорах, а также добавлять и редактировать их.
Меняется только название и используемые модель с формой.

Остается только одна отличная от других  функция `conference_authors` - она формирует словарь авторов для данной конференции на основе регистраций.
Таким образом, она отображает спискок авторов, зарегистрированных на выранную конференцию.
```
def conference_authors(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    # Получаем все регистрации для данной конференции
    registrations = Registration.objects.filter(conference=conference)
    # Формируем словарь, где ключи - конференции, значения - списки авторов
    authors_by_conference = {}
    for registration in registrations:
        if registration.conference not in authors_by_conference:
            authors_by_conference[registration.conference] = []
        authors_by_conference[registration.conference].append({'author': registration.author, 'title': registration.title})
    return render(request, 'conference_authors.html', {'authors_by_conference': authors_by_conference})
```