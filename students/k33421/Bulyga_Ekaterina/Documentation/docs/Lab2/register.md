<h1>Шаблон Register</h1>

<pre>
<code>
{% load static %}
&lt!DOCTYPE html&gt
&lthtml lang="en"&gt
&lthead&gt
    &ltmeta charset="UTF-8"&gt
    &lttitle&gtРегистрация&lt/title&gt
    &ltlink rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"&gt
&lt/head&gt
&ltbody&gt
{% include 'conferences/navbar.html' %}
&ltbr&gt
&ltdiv class="col-md-6 offset-md-3"&gt
    &lth1&gtРегистрация&lt/h1&gt
    &ltbr&gt
    &ltform method="post" action=""&gt
        {% csrf_token %}

        {{ form.as_p }}

        &ltbr/&gt
        &ltbutton type="submit" class="btn btn-primary"&gtРегистрация&lt/button&gt
    &lt/form&gt
&lt/div&gt

&lt/body&gt
&ltscript src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"&gt&lt/script&gt
&ltscript src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"&gt&lt/script&gt
&ltscript src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"&gt&lt/script&gt
&lt/html&gt
</code>
</pre>
