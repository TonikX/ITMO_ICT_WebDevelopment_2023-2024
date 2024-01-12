Подгружены все используемые шаблоны:
    {% extends 'base.html' %}
    
    {% block title %}All comments{% endblock %}
    
    {% block content %}
        <table class="table table-hover table-bordered">
            <thead class="table-info">
                <tr>
                    <th scope="col">Отель</th>
                    <th scope="col">Номер комнаты</th>
                    <th scope="col">Автор</th>
                    <th scope="col">Дата заселения</th>
                    <th scope="col">Дата выселения</th>
                    <th scope="col">Отзыв</th>
                </tr>
            </thead>
            {% for comment in object_list %}
            <tbody>
                <tr>
                    <td>{{ comment.reservation.room.hotel.name }}</td>
                    <td>{{ comment.reservation.room.number_room }}</td>
                    <td>{{ comment.guest }}</td>
                    <td>{{ comment.date_start }}</td>
                    <td>{{ comment.date_end }}</td>
                    <td>{{ comment.text }}</td>
                </tr>
            </tbody>
            {% endfor %}
        </table>
    {% endblock %}

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
        <title> {% block title %} {% endblock %} </title>
    </head>
    <body>
        {% include "navigation.html" %}
        {% block content %}
        {% endblock %}
    </body>
    </html>

    {% extends 'base.html' %}
    {% load crispy_forms_tags %}
    {% block title %}Comment{% endblock %}
    
    {% block content %}
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-8">
              <h1 class="mt-2">Оставьте свой отзыв</h1>
              <hr class="mt-0 mb-4">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form|crispy }}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="submit" class="btn btn-success g-5">Сохранить</button>
                      </div>
                </form>
            </div>
          </div>
        </div>
    {% endblock %}

    {% extends 'base.html' %}
    {% load crispy_forms_filters %}
    
    {% block title %}Reservation{% endblock %}
    
    {% block content %}
    {% load crispy_forms_tags %}
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-8">
              <h1 class="mt-2">Бронирование комнаты</h1>
              <hr class="mt-0 mb-4">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form|crispy }}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="submit" class="btn btn-success g-5">Сохранить</button>
                      </div>
                </form>
            </div>
          </div>
        </div>
    {% endblock %}

    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
      <title>Delete book</title>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
              <div class="col-8">
                <h2 class="mt-2">Удаление резервирования</h2>
                <hr class="mt-0 mb-4">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div>
                            <p class = "d-flex justify-content-end"></p>Вы действительно хотите удалить "{{ object }}"?</p>
                        </div>
                        <div>
                            <input type="submit" value="Подтвердить" class="btn btn-danger p-2 "></input>
                        </div>
                    </form>
                    
                </div>
              </div>
            </div>
        </body>
    </html>
    
    {% extends 'base.html' %}   
    {% block title %}All guests{% endblock %}
    
    {% block content %}
        <h1 class="d-flex justify-content-center"> Гости отелей </h1>
        <table class="table table-hover table-bordered">
            <thead class="table-info">
                <tr>
                    <th scope="col">Отель</th>
                    <th scope="col">Фамилия</th>
                    <th scope="col">Имя</th>
                </tr>
            </thead>
            {% for user in object_list %}
            <tbody>
                <tr>
                    <td>{{ user.hotel}}</td>
                    <td>{{ user.guest.last_name }}</td>
                    <td>{{ user.guest.first_name }}</td>
                </tr>
            </tbody>
            {% endfor %}
        </table>
    {% endblock %}