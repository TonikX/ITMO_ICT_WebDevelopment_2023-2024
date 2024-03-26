<h1>Шаблон Conferences</h1>

<pre>
<code>
{% extends 'conferences/main.html' %}

{% load custom_tags %}

{% block content%}

&ltbr&gt


&ltdiv class="row"&gt
    &ltdiv class="col-md"&gt
        &ltdiv class="card card-body"&gt
            &lth5&gtСписок моих регистраций&lt/h5&gt
        &lt/div&gt
        &ltdiv class="card card-body"&gt
            &lttable class="table"&gt
                &lttr&gt
                    &ltth style="width: 35%"&gtНазвание&lt/th&gt
                    &ltth style="width: 35%"&gtТема&lt/th&gt
                    &ltth style="text-align: center; width: 30%"&gtРедактирование&lt/th&gt
                &lt/tr&gt

                {% for conf, topic in conference_to_topic.items %}
                    &lttr&gt
                        &lttd&gt{{ conf.name }}&lt/td&gt
                        &lttd&gt{{ topic }}&lt/td&gt
                        &lttd align="center"&gt
                            &ltdiv class="row"&gt
                                &ltdiv class="col-md"&gt
                                    &ltbutton type="button" style="width: 95%" class="btn btn-info" data-toggle="modal" data-target="#modal{{ conf.id }}"&gtИзменить тему&lt/button&gt
                                &lt/div&gt
                                &ltdiv class="col-md"&gt
                                    &ltform method="post" action="/my_registrations/cancel_registration/"&gt
                                        {% csrf_token %}
                                        &ltinput type="hidden" name="conf_id" value="{{ conf.id }}"&gt
                                        &ltbutton type="submit" class="btn btn-danger"&gtОтмена регистрации&lt/button&gt
                                    &lt/form&gt
                                &lt/div&gt
                            &lt/div&gt
                        &lt/td&gt
                    &lt/tr&gt
                &ltdiv class="modal fade" id="modal{{ conf.id }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"&gt
                    &ltdiv class="modal-dialog" role="document"&gt
                        &ltdiv class="modal-content"&gt
                            &ltdiv class="modal-header"&gt
                                &lth5 class="modal-title" id="exampleModalLabel"&gtИзменение темы&lt/h5&gt
                            &lt/div&gt
                            &ltform method="post" id="modalChange" action="/my_registrations/save_registration/"&gt
                                {% csrf_token %}
                                &ltdiv class="modal-body"&gt
                                    &ltdiv class="form-group"&gt
                                        &ltinput type="text" class="form-control" name="topic"
                                               placeholder="Новая тема выступления"
                                               oninvalid="this.setCustomValidity('Введите тему')"
                                               oninput="setCustomValidity('')" required&gt
                                        &ltinput type="hidden" name="conf_id" value="{{ conf.id }}"&gt
                                    &lt/div&gt
                                &lt/div&gt
                                &ltdiv class="modal-footer"&gt
                                    &ltbutton type="button" class="btn btn-secondary" data-dismiss="modal"&gtОтмена&lt/button&gt
                                    &ltbutton type="submit" form="modalChange" class="btn btn-primary"&gtСохранить&lt/button&gt
                                &lt/div&gt
                            &lt/form&gt
                        &lt/div&gt
                    &lt/div&gt
                &lt/div&gt
                {% endfor %}
            &lt/table&gt
        &lt/div&gt
    &lt/div&gt
&lt/div&gt



{% endblock %}
</code>
</pre>
