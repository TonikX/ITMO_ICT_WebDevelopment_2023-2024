# Реализация интерфейсов

## home.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на наш сайт Гонки.ru</h1>
    
        <button onclick="showRaceInfo()">Информация о гонках</button>
    
        {% if user.is_authenticated %}
            <button onclick="registerForRace()">Зарегистрироваться на гонку</button>
            <button onclick="registrationsList()">Ваши регистрации</button>
            <button onclick="racerProfile()">Профиль гонщика</button>
            <button onclick="logout()">Выйти</button>
        {% endif %}
    
        {% if not user.is_authenticated %}
            <button onclick="login()">Вход</button>
            <button onclick="registration()">Регистрация</button>
        {% endif %}
    
        <script>
            function showRaceInfo() {
                window.location.href = '/races/';
            }
    
            function registerForRace() {
                window.location.href = '/race_registration/';
            }
    
            function racerProfile() {
                window.location.href = '/racer_profile/';
            }
    
            function registrationsList() {
                window.location.href = '/registrations/';
            }
    
            function logout() {
                window.location.href = '/logout/';
            }
    
            function login() {
                window.location.href = '/login/';
            }
    
            function registration() {
                window.location.href = '/register/';
            }
        </script>
    </body>
    </html>

## login.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Авторизация</title>
    </head>
    <body>
        <h2>Авторизация</h2>
        {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
        <form method="post">
            {% csrf_token %}
            <label for="username">Имя пользователя:</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Пароль:</label>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Войти">
        </form>
    
        <button onclick="back()">Зарегистрироваться</button>
        <script>
            function back() {
                window.location.href = '/register';
            }
        </script>
    </body>
    </html>

## register.html

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
            <input type="submit" value="Зарегистрироваться">
        </form>
        <p>
            Уже есть аккаунт? <a href="{% url 'login' %}">Войти</a>
        </p>
    
        <button onclick="back()">Назад</button>
        <script>
            function back() {
                window.location.href = '/';
            }
        </script>
    </body>
    </html>

## add_comment.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Добавить комментарий</title>
    </head>
    <body>
        <h1>Добавить комментарий к гонке: {{ race.title }}</h1>
    
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Добавить комментарий</button>
        </form>
    
        <button onclick="back()">Назад</button>
        <script>
            function back() {
                window.location.href = '/races/race/{{ race.id }}';
            }
        </script>
    </body>
    </html>

## racer_profile.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Профиль гонщика</title>
    </head>
    <body>
        <h1>Профиль гонщика</h1>
        <p>*Если вы хотите участвовать в гонках, необходимо иметь заполненный профиль гонщика.</p>
    
        <form method="post">
            {% csrf_token %}
            {{ profile_form.as_p }}
            {{ car_form.as_p }}
            <button type="submit">Сохранить</button>
        </form>
    
        <button onclick="back()">Назад</button>
    
        <script>
            function back() {
                window.location.href = '/';
            }
        </script>
    </body>
    </html>

## race_detail.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Информация о гонке: {{ race.title }}</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
    
            table, th, td {
                border: 1px solid black;
            }
    
            th, td {
                padding: 10px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Информация о гонке</h1>
        <h2>Название: {{ race.title }}</h2>
        <p>Дата: {{ race.date }}</p>
        <p>Локация: {{ race.location }}</p>
        <p>Описание: {{ race.description }}</p>
    
        {% if registrations %}
            <h2>Участники гонки (зарегистрированные):</h2>
            <table>
                <thead>
                    <tr>
                        <th>Гонщик</th>
                        <th>Команда</th>
                    </tr>
                </thead>
                <tbody>
                    {% for registration in registrations %}
                        <tr>
                            <td>{{ registration.racer.first_name }} {{ registration.racer.last_name }}</td>
                            <td>{{ registration.racer.team_name }}</td>
                        </tr>
                    {% empty %}
                        <tr>
                            <td colspan="2">Для этой гонки нет зарегистрированных участников.</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% endif %}
    
        {% if race_results %}
            <h2>Результаты гонки:</h2>
            <table>
                <thead>
                    <tr>
                        <th>Гонщик</th>
                        <th>Команда</th>
                        <th>Описание</th>
                        <th>Опыт</th>
                        <th>Авто</th>
                        <th>Позиция</th>
                        <th>Время</th>
                        <th>Максимальная скорость (км/ч)</th>
                    </tr>
                </thead>
                <tbody>
                    {% for result in race_results %}
                        <tr>
                            <td>{{ result.racer.first_name }} {{ result.racer.last_name }}</td>
                            <td>{{ result.racer.team_name }}</td>
                            <td>{{ result.racer.participant_description }}</td>
                            <td>{{ result.racer.experience }}</td>
                            <td>{{ result.racer.car.brand }}, {{ result.racer.car.model }}</td>
                            <td>{{ result.position }}</td>
                            <td>{{ result.lap_time }}</td>
                            <td>{{ result.top_speed }}</td>
                        </tr>
                    {% empty %}
                        <tr>
                            <td colspan="4">Для этой гонки нет результатов.</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% endif %}
    
        <h2>Комментарии к гонке:</h2>
        <ul>
            {% for comment in comments %}
                <li>
                    <p>Автор: {{ comment.commentator.username }}</p>
                    <p>Дата: {{ comment.comment_date }}</p>
                    <p>Тип комментария: {{ comment.comment_type }}</p>
                    <p>Рейтинг: {{ comment.rating }}</p>
                    <p>{{ comment.comment_text }}</p>
                </li>
            {% empty %}
                <li>Для этой гонки нет комментариев.</li>
            {% endfor %}
        </ul>
    
        <h1></h1>
        <button onclick="back()">Назад</button>
        {% if user.is_authenticated %}
            <button onclick="comments()">Добавить комментарии</button>
        {% endif %}
        <script>
            function back() {
                window.location.href = '/races';
            }
            function comments() {
                window.location.href = '/races/race/add_comment/{{ race.id }}';
            }
        </script>
    </body>
    </html>

## race_list.html
    
    <!DOCTYPE html>
    <html>
    <head>
        <title>Список гонок</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
    
            table, th, td {
                border: 1px solid black;
            }
    
            th, td {
                padding: 10px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Список гонок</h1>
    
        <table>
            <thead>
                <tr>
                    <th>Название</th>
                    <th>Дата</th>
                    <th>Локация</th>
                    <th>Действие</th>
                </tr>
            </thead>
            <tbody>
                {% for race in races %}
                    <tr>
                        <td>{{ race.title }}</td>
                        <td>{{ race.date }}</td>
                        <td>{{ race.location }}</td>
                        <td>
                            <a href="{% url 'race_detail' race.id %}">Подробнее</a>
                        </td>
                    </tr>
                {% empty %}
                    <tr>
                        <td colspan="4">На данный момент нет доступных гонок.</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    
        <h1></h1>
        <button onclick="back()">Назад</button>
    
        <script>
            function back() {
                window.location.href = '/';
            }
        </script>
    </body>
    </html>

## race_registration.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Регистрация на гонки</title>
    </head>
    <body>
        <h1>Регистрация на гонки</h1>
    
        <ul>
            {% for race in upcoming_races %}
                <li>
                    Гонка: {{ race.title }}
                    <p>Дата: {{ race.date }}</p>
                    <p>Локация: {{ race.location }}</p>
                    <form method="post">
                        {% csrf_token %}
                        <input type="hidden" name="race_id" value="{{ race.id }}">
                        {% if race.date >= current_datetime %}
                            <button type="submit">Зарегистрироваться</button>
                        {% endif %}
                    </form>
                </li>
            {% empty %}
                <p>На данный момент нет предстоящих гонок, на которые вы еще не зарегистрированы.</p>
            {% endfor %}
        </ul>
    
        <button onclick="back()">Назад</button>
        <script>
            function back() {
                window.location.href = '/';
            }
        </script>
    </body>
    </html>

## registration_delete.html

    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Удаление регистрации</title>
    </head>
    
    <body>
      <form method="post">{% csrf_token %}
        <p>Вы уверены, что хотите удалить регистрацию на гонку"{{ object }}"?</p>
        <input type="submit" value="Удалить">
      </form>
    
     <button onclick="back()">Назад</button>
    
        <script>
            function back() {
                window.location.href = '/';
            }
        </script>
    </body>
    </html>

## registration_list.html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Регистрации</title>
    </head>
    <body>
        <h1>Ваши регистрации</h1>
        <ul>
            {% for registration in registrations %}
                <li>
                    <p>Гонка: {{ registration.race.title }}<p>
                    <p>Дата: {{ registration.race.date }}</p>
                    <p>Локация: {{ registration.race.location }}</p>
                    <form method="post">
                        {% csrf_token %}
                        <input type="hidden" name="registration_id" value="{{ registration.id }}">
                        {% if registration.race.date > current_datetime %}
                            <button type="submit">Удалить</button>
                        {% endif %}
                    </form>
                </li>
            {% empty %}
                <p>Вы не зарегистрированы ни на одну гонку.</p>
            {% endfor %}
        </ul>
        <button onclick="back()">Назад</button>
    
        <script>
            function back() {
                window.location.href = '/';
            }
        </script>
    </body>
    </html>
