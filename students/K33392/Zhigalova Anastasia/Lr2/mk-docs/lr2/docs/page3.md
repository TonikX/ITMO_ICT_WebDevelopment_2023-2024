# Realization html

### add_review.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Добавить отзыв</title>
</head>
<body>
    <h1>Добавить отзыв для конференции "{{ conference.title }}"</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Отправить отзыв</button>
    </form>
    <a href="{% url 'review_list' conference.id %}">Посмотреть отзывы</a>
</body>
</html>

```

### create_registration.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Регистрация на конференцию</title>
</head>
<body>
    <h1>Регистрация на конференцию</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Зарегистрироваться</button>
    </form>
    <button type="submit"> <a href="{% url 'index' %}">Назад к главной странице</a></button>
</body>
</html>
```

### delete_registration.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Удаление регистрации</title>
</head>
<body>
    <h1>Вы действительно хотите удалить регистрацию "{{ registration.conference.title }}"?</h1>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Удалить</button>
    </form>
</body>
</html>
```

### edit_registration.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Редактирование регистрации</title>
</head>
<body>
    <h1>Редактирование регистрации</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Сохранить изменения</button>
    </form>
</body>
</html>
```

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Главная страница конференции</title>
</head>
<body>
    <h1>Добро пожаловать на сайт конференций!</h1>
    <nav>
        <a href="{% url 'index' %}">Главная</a> |
        <a href="{% url 'list_conferences' %}">Конференции</a> |
        <a href="{% url 'my_registrations' %}">Мои регистрации</a> |
        <a href="{% url 'create_registration' %}">Добавить регистрацию</a>
    </nav>
    {% if user.is_authenticated %}
        <p>Привет, {{ user.username }}!</p>
        <a href="{% url 'logout' %}">Выйти</a>
    {% else %}
        <a href="{% url 'register' %}">Регистрация</a> |
        <a href="{% url 'login' %}">Вход</a>
    {% endif %}
</body>
</html>
```

### list.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Список конференций</title>
</head>
<body>
    <h1>Конференции</h1>
    <ul>
        {% for conference in conferences %}
            <li>{{ conference.title }} - {{ conference.venue }} ({{ conference.start_date }} - {{ conference.end_date }})</li>
            <a href="{% url 'add_review' conference.id %}">Добавить отзыв</a>
        {% endfor %}
    </ul>

    <h2>Регистрации на конференции</h2>
    <ul>
        {% for registration in registrations %}
            <li>{{ registration.user.username }} зарегистрирован на конференцию "{{ registration.conference.title }}" (Дата регистрации: {{ registration.date_registered }})</li>
        {% endfor %}
    </ul>

    <h2>Список участников</h2>
    <table border="1">
        <tr>
            <th>Имя пользователя</th>
            <th>Зарегистрированные конференции</th>
            <th>Дата регистрации</th>
            <th>Рекомендовано к публикации</th>
        </tr>
        {% for registration in registrations %}
            <tr>
                <td>{{ registration.user.username }}</td>
                <td>{{ registration.conference.title }}</td>
                <td>{{ registration.date_registered }}</td>
                <td>{{ registration.recommended_for_publication|yesno:"Да,Нет" }}</td>
            </tr>
        {% endfor %}
    </table>
    
    <a href="{% url 'index' %}">Главная</a>
</body>
</html>
```

### my_registrations.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Мои регистрации</title>
</head>
<body>
    <h1>Мои регистрации на конференции</h1>
    <table>
        <tr>
            <th>Конференция</th>
            <th>Дата регистрации</th>
            <th>Действия</th>
        </tr>
        {% for registration in registrations %}
        <tr>
            <td>{{ registration.conference.title }}</td>
            <td>{{ registration.date_registered }}</td>
            <td>
                <a href="{% url 'edit_registration' registration.id %}">Редактировать</a>
                <a href="{% url 'delete_registration' registration.id %}" onclick="return confirm('Вы уверены, что хотите удалить регистрацию?');">Удалить</a>
            </td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="3">Регистрации отсутствуют.</td>
        </tr>
        {% endfor %}
    </table>
    <a href="{% url 'index' %}">Вернуться на главную страницу</a>
</body>
</html>
```

### register.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Регистрация</title>
</head>
<body>
  <h2>Регистрация</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Зарегистрироваться</button>
  </form>
  <button type="submit"><a href="{% url 'login' %}">Войти</a></button>
</body>
```

### reviews_list.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Отзывы конференции {{ conference.title }}</title>
</head>
<body>
    <h1>Отзывы конференции {{ conference.title }}</h1>
    <ul>
        {% for review in reviews %}
        <li>
            <strong>{{ review.author.username }}</strong> ({{ review.comment_date }}): 
            Оценка: {{ review.rating }}<br>
            {{ review.text }}
        </li>
        {% empty %}
        <li>Отзывов пока нет.</li>
        {% endfor %}
    </ul>
    <a href="{% url 'list_conferences' %}">Конференции</a>
</body>
</html>
```
