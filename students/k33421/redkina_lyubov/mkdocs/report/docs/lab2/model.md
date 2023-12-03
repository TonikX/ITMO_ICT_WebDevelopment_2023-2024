### models.py


Модель в Django является способом описания структуры данных созданного приложения. 
Она определяет, какие данные будут сохраняться в базе данных и как они будут организованы.

В этой части кода я импортирую необходимые модули для определения моделей в Django. `models` предоставляет базовые классы для создания моделей базы данных, а `AbstractUser` - базовую модель пользователя Django, которую можно расширить для создания своей модели пользователя.
```
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
```

Здесь создается модель `Author`, которая расширяет `AbstractUser`. Я добавляю несколько дополнительных полей: `first_name`, `last_name`, `occupation` (занятие), `is_admin` (статус администратора), а также поля для связи с группами и разрешениями Django.

```
class Author(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', related_name='author_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='author_user_permissions')
```

Эта часть кода определяет модель `Conference` с несколькими полями, такими как `title` (заголовок), `topics` (темы), `venue` (место проведения), `date_from` и `date_to` (даты начала и окончания).

```
class Conference(models.Model):
    title = models.CharField(max_length=200)
    topics = models.TextField()
    venue = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
```

Здесь определена модель `Registration` с внешними ключами на модели `Author` и `Conference`. Есть также поля `title` и `approved_reg` для заголовка и статуса утверждения.

```
class Registration(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    approved_reg = models.BooleanField(default=False)
```

Эта часть кода определяет модель `Presentation` с внешними ключами на модели `Conference` и `Author`. Есть поля `title` и `approved_pres` для заголовка и статуса утверждения.

```
class Presentation(models.Model):
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    approved_pres = models.BooleanField(default=False)
```

Здесь определена модель `Review` с внешними ключами на модели `Conference` и `Author`. Есть также поля `comment_date`, `text` и `rating` для даты комментария, текста комментария и рейтинга (с валидацией от 1 до 10).

```
class Review(models.Model):
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
```

