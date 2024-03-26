<h1>Шаблон Participants</h1>

<pre>
<code>
{% extends 'conferences/main.html' %}

{% load custom_tags %}

{% block content%}

&ltbr&gt


&ltdiv class="row"&gt
    &ltdiv class="col-md"&gt
        &ltdiv class="card card-body"&gt
            &lth5&gtCписок участников конференций&lt/h5&gt
        &lt/div&gt
        &ltdiv class="card card-body"&gt
            &lttable class="table"&gt
                &lttr&gt
                    &ltth&gtКонференция&lt/th&gt
                    &ltth&gtУчастники&lt/th&gt
                &lt/tr&gt

                {% for conf_name, participants_list in participants.items %}
                    &lttr&gt
                        &lttd&gt{{ conf_name }}&lt/td&gt
                        &lttd&gt{% convert_list_to_string participants_list %}&lt/td&gt
                    &lt/tr&gt
                {% endfor %}
            &lt/table&gt
        &lt/div&gt
    &lt/div&gt
&lt/div&gt



{% endblock %}
</code>
</pre>
