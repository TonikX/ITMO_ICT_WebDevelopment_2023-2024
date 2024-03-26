<h1>Шаблон Navbar</h1>

<pre>
<code>
{% load static %}

&ltnav class="navbar navbar-expand-lg navbar-dark bg-dark"&gt
  &ltimg src="{% static 'images/logo.png' %}" height="45px"&gt
  &ltbutton class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation"&gt
    &ltspan class="navbar-toggler-icon"&gt&lt/span&gt
  &lt/button&gt
  &ltdiv class="collapse navbar-collapse" id="navbarNavAltMarkup"&gt
    &ltdiv class="navbar-nav"&gt
      {% if user.is_authenticated %}
      &lta class="nav-item nav-link" href="/"&gtКонференции&lt/a&gt
      &lta class="nav-item nav-link" href="/my_registrations/"&gtМои регистрации&lt/a&gt
      &lta class="nav-item nav-link" href="/participants/"&gtУчастники&lt/a&gt
      &lta class="nav-item nav-link" href="/logout/"&gtВыход&lt/a&gt
      {% else %}
      &lta class="nav-item nav-link" href="/"&gtАвторизация&lt/a&gt
      &lta class="nav-item nav-link" href="/register/"&gtРегистрация&lt/a&gt
      {% endif %}
    &lt/div&gt
  &lt/div&gt
&lt/nav&gt
</code>
</pre>
