# Темплэйты

### Обертка
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Lab 2</title>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="collapse navbar-collapse" id="navbarText">
            <a class="nav-link active" aria-current="page" href="{% url 'flights_list' %}">All flight</a>
            {% if user.is_authenticated %}

            <a class="nav-link active" aria-current="page" href="{% url 'reservations_for_user' %}">
                Your reservations  </a>
            {% endif %}
            <br><br>
            {% if user.is_authenticated %}

            You have logged as {{ user.username }}. Click here to <a class="dropdown-item" href="{% url 'logout' %}">Logout</a></br>

            {% else %}
            <a href="{% url 'user_login' %}" class="mr-2">
                <button class="btn btn-outline-primary btn-sm" type="submit">Login</button>
            </a>
            <a href="{% url 'register' %}">
                <button class="btn btn-outline-primary btn-sm" type="submit">Register</button>
            </a>
            {% endif %}
        </div>
</nav>

<div class="container py-3">
    {% block content %} {% endblock %}
</div>
</body>
</html>
```

### Логин 
```
{% extends 'base.html' %} {% block content %}

<h2 class="mb-3">Sign in</h2>
<form method="post" class="mb-3">
    {% csrf_token %}
    {{ user_form.as_p }}
    <button type="submit" class="btn btn-primary">Sign in</button>
</form>
{% endblock %}
```

### Регистрация 

```
{% extends 'base.html' %} {% block content %}

<h2 class="mb-4">Registration</h2>
<form method="post" class="mb-3">
    {% csrf_token %}
    {{ user_form.as_p }}
    <button type="submit" class="btn btn-primary">Register</button>
</form>
<p>Already have a profile? <a href="{% url 'user_login' %}" class="text-primary">Login</a></p>

{% endblock %}

```

### Список полетов

```
{% extends 'base.html' %} {% block content %}

<h1 class="text-center">Schedule{% if city %} {{city}} {% endif %} {% if airline %} {{airline}} {% endif %}</h1>


<form method="GET" class='mb-5'>

  <div class='mb-3'>
    <label for="citySearchSelect" class="form-label">City: </label>
    <select id="citySearchSelect" name="city" class="form-select form-select-lg ">
      <option value="">Choose the city</option>
      {% for available_city in available_cities %}
        <option
          value="{{available_city.name}}"
          {% if city == available_city.name %} selected {% endif %}
        >
          {{available_city.name}}
        </option>
      {% endfor %}
    </select>
  </div>

    <div class='mb-3'>
    <label for="airlineSearchSelect" class="form-label">airline: </label>
    <select id="airlineSearchSelect" name="airline" class="form-select form-select-lg ">
      <option value="">Choose the airline</option>
      {% for available_airline in available_airlines %}
        <option
          value="{{available_airline.name}}"
          {% if airline == available_airline.name %} selected {% endif %}
        >
          {{available_airline.name}}
        </option>
      {% endfor %}
    </select>
  </div>

  <button type="submit" class="btn btn-primary">Find</button>
</form>

<table class="table table-striped table-hover mb-5">
  <thead>
    <tr>
      <th scope="col">Type:</th>
      <th scope="col">Time From:</th>
      <th scope="col">Time To:</th>
      <th scope="col">Flight Num:</th>
      <th scope="col">Direction From:</th>
      <th scope="col">Direction To:</th>
      <th scope="col">Airline:</th>
      <th scope="col">Plane model:</th>
      <th scope="col">Extra:</th>
    </tr>
  </thead>

  <tbody>
    {% for flight in flights %}
      <tr>
        <td>{{flight.type}}</td>
        <td>{{flight.departure_time}}</td>
        <td>{{flight.arrival_time}}</td>
        <td>{{flight.flight_number}}</td>
        <td>{{flight.arrival_city.name}}</td>
        <td>{{flight.departure_city.name}}</td>
        <td>{{flight.air_line.name}}</td>
        <td>{{flight.plane.name}}</td>
        <td><a href="{% url 'flight_detail' flight.id %}">Details</a></td>
      </tr>
    {% endfor %}
  </tbody>
</table>

{% endblock %}
```

### Детали полета

```
{% extends 'base.html' %} {% block content %}

<h1>FLight {{flight.name}}</h1>

<h2 class="mb-3">Information about flight</h2>
<div>Flight number: {{ flight.flight_number }}</div>
<div>Airline: {{ flight.air_line }}</div>
<div>Departure: {{ flight.departure_city }} {{ flight.departure }}</div>
<div>Arrival: {{ flight.arrival_city }} {{ flight.arrival }}</div>
<div>Type: {{ flight.type }}</div>
<div>Gate: {{ flight.gate }}</div>


<h2>Passengers</h2>
<div class="row mb-5">
  <div class="col-md-5">
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th scope="col">Username</th>
          <th scope="col">Seat</th>
        </tr>
      </thead>

      <tbody>
        {% for ticket in tickets %}
          <tr>
            <td class="align-middle">{{ticket.passenger.last_name}} {{ticket.passenger.first_name}} </td>
            <td class="align-middle">{{ticket.seat}}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<h4 class="my-3">Comments</h4>
<ul class="list-group">
    {% for comment in comments %}
    <li class="list-group-item">
        <strong>{{ comment.author.username }}</strong>
        <br>
        Rating: {{ comment.rating }}
        <br>
        {{ comment.text }}
    </li>
    {% endfor %}
</ul>


<h2>Seats</h2>
<table class="table table-striped table-hover mb-5">
  {% for seat in seats %}
  <td class="text-center">
    {% if seat.is_taken %} <s style="color:grey;">{{seat.name}}</s>
    {% else %} {{seat.name}}
    {% endif %}
  </td>
  {% endfor %}
</table>

<h2>Reserve  a seat</h2>
{% if user.is_authenticated %}
<div class="row">
  <div class="col-md-3">
    <form method="post">
      {% csrf_token %}
      <div class="mb-3">
        <label for="ticketSeatInput" class="form-label">Seat: </label>
        <input name='seat' class="form-control" id="ticketSeatInput">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</div>
  {% if has_ticket%}
  <td><a href="{% url 'reservations_for_user'%}">You already have a ticket on these flight</a></td>
  {% endif %}

<h5 class="my-3">Add comment</h5>
<form method="post" class="mb-5">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <button type="submit" class="btn btn-primary">Add</button>
</form>

{% else %}
<td><a href="{% url 'register' %}">Register</a> previously</td>
{% endif %}

{% endblock %}
```

### Список броней

```
{% extends 'base.html' %} {% block content %}

<h2 class="mb-4">Your reservations</h2>
<table class="table table-bordered">
    <thead class="thead-light">
    <tr>
        <th scope="col">Seat</th>
        <th scope="col">Ticket</th>
        <th scope="col">Flight</th>
        <th scope="col">FlightLink</th>
    </tr>
    </thead>
    <tbody>
    {% for reservation in reservations %}
    <tr>
        <td>{{ reservation.seat}}</td>
        <td>{{ reservation.ticket_number}}</td>
        <td>
            <div>Flight number: {{ reservation.flight.flight_number }}</div>
            <div>Airline: {{ reservation.flight.air_line }}</div>
            <div>Departure: {{ reservation.flight.departure_city }} {{ reservation.flight.departure }}</div>
            <div>Arrival: {{ reservation.flight.arrival_city }} {{ reservation.flight.arrival }}</div>
            <div>Gate: {{ reservation.flight.gate }}</div>
        </td>
        <td><a href="{% url 'flight_detail' reservation.flight.id %}" class="btn btn-primary">More</a></td>
        <td><a href="{% url 'reservation_update' reservation.id %}" class="btn btn-primary">Change</a></td>
    </tr>
    {% endfor %}
    </tbody>
</table>

{% endblock %}
```

### Изменение брони

```
{% extends 'base.html' %} {% block content %}

<a href="{% url 'flight_detail' reservation.flight.id %}" class="btn btn-secondary mb-4">Back to flight</a>

<h2>Change seat</h2>
<h5 class="my-3">Information about reservation</h5>
<div>Old seat: {{ reservation.seat }}</div>
<div>Ticket: {{ reservation.ticket_number }}</div>

<form method="POST" class="mt-3">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit" class="btn btn-primary">Save changes</button> <a href="{% url 'reservation_delete' reservation.id %}" class="btn btn-primary"> or Delete</a>
</form>



{% endblock %}
```

### Удаление брони

```
{% extends 'base.html' %} {% block content %}

<a href="{% url 'flight_detail' reservation.flight.id %}" class="btn btn-secondary mb-4">Back to flight</a>

<h2>Delete reservation</h2>
<h5 class="my-3">Information about reservation</h5>
<div>Seat: {{ reservation.seat }}</div>
<div>Ticket: {{ reservation.ticket_number }}</div>

<form method="POST" class="mt-3">
    {% csrf_token %}
    <p>Are you sure you want to delete reservation?</p>

    <button type="submit" class="btn btn-danger">Delete</button>
</form>

{% endblock %}
```
