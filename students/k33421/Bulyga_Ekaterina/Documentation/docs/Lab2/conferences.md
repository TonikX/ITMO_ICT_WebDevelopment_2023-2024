<h1>Шаблон Conferences</h1>


<pre>
<code>
{% extends 'conferences/main.html' %}

{% load custom_tags %}

{% block content %}

&ltbr&gt


&ltdiv class="row"&gt
    &ltdiv class="col-md"&gt
        &ltdiv class="card card-body"&gt
            &lth5&gtСписок конференций&lt/h5&gt
        &lt/div&gt
        &ltdiv class="card card-body"&gt
            &lttable class="table"&gt
                &lttr&gt
                    &ltth&gtНазвание&lt/th&gt
                    &ltth&gtТемы&lt/th&gt
                    &ltth&gtМесто&lt/th&gt
                    &ltth&gtДата&lt/th&gt
                    &ltth&gtОписание&lt/th&gt
                    &ltth&gtОписание места&lt/th&gt
                    &ltth&gtУсловия участия&lt/th&gt
                    &ltth style="text-align: center"&gtРегистрация&lt/th&gt
                    &ltth style="text-align: center"&gtОтзыв&lt/th&gt
                &lt/tr&gt

                {% for conf in conferences %}
                    &lttr&gt
                        &lttd&gt{{conf.name}}&lt/td&gt
                        &lttd&gt{{topics|get_item:conf.id|join:", "}}&lt/td&gt
                        &lttd&gt{{conf.location}}&lt/td&gt
                        &lttd&gt{{conf.date}}&lt/td&gt
                        &lttd&gt{{conf.description}}&lt/td&gt
                        &lttd&gt{{conf.location_description}}&lt/td&gt
                        &lttd&gt{{conf.participating_terms}}&lt/td&gt
                        &lttd align="center"&gt
                            {% if conf.id in registered %}
                                &ltbutton type="button" disabled class="btn btn-success"&gtВы зарегистрированы&lt/button&gt
                            {% else %}
                                &ltbutton type="button" class="btn btn-info" data-toggle="modal" data-target="#modal{{ conf.id }}"&gtРегистрация&lt/button&gt
                            {% endif %}

                        &lt/td&gt
                        &lttd align="center"&gt
                            &ltbutton type="button" class="btn btn-secondary" data-toggle="modal" data-target="#reviewModal{{ conf.id }}"&gtОтзывы&lt/button&gt
                        &lt/td&gt
                    &lt/tr&gt
                &ltdiv class="modal fade" id="modal{{ conf.id }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"&gt
                    &ltdiv class="modal-dialog" role="document"&gt
                        &ltdiv class="modal-content"&gt
                            &ltdiv class="modal-header"&gt
                                &lth5 class="modal-title" id="exampleModalLabel"&gtРегистрация&lt/h5&gt
                            &lt/div&gt
                            &ltform method="post" action="save_registration/"&gt
                                {% csrf_token %}
                                &ltdiv class="modal-body"&gt
                                    &ltdiv class="form-group"&gt
                                        &ltinput type="text" class="form-control" name="topic" placeholder="Тема выступления" required oninvalid="this.setCustomValidity('Введите тему')" oninput="setCustomValidity('')"&gt
                                        &ltinput type="hidden" name="conf_id" value="{{ conf.id }}"&gt
                                    &lt/div&gt
                                &lt/div&gt
                                &ltdiv class="modal-footer"&gt
                                    &ltbutton type="button" class="btn btn-secondary" data-dismiss="modal"&gtОтмена&lt/button&gt
                                    &ltbutton type="submit" class="btn btn-primary"&gtСохранить&lt/button&gt
                                &lt/div&gt
                            &lt/form&gt
                        &lt/div&gt
                    &lt/div&gt
                &lt/div&gt
                &ltdiv class="modal fade" id="reviewModal{{ conf.id }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"&gt
                    &ltdiv class="modal-dialog" role="document"&gt
                        &ltdiv class="modal-content"&gt
                            &ltdiv class="modal-header"&gt
                                &lth5 class="modal-title" id="reviewModalLabel"&gtОтзывы&lt/h5&gt
                                &ltbutton type="button" class="close" data-dismiss="modal" aria-label="Close"&gt
                                    &ltspan aria-hidden="true"&gt&times;&lt/span&gt
                                &lt/button&gt
                            &lt/div&gt
                            &ltform  method="post" action="/save_review/"&gt
                                {% csrf_token %}
                                &ltdiv class="modal-body"&gt
                                    &ltdiv class="form-group"&gt
                                        &ltlabel for="reviewText"&gtОставьте отзыв и рейтинг&lt/label&gt
                                        &lttextarea name="reviewText" class="form-control" id="reviewText" rows="3" required&gt&lt/textarea&gt
                                        &ltinput type="hidden" name="conf_id" value="{{ conf.id }}"&gt
                                        &ltbr&gt
                                        &ltdiv class="row"&gt
                                            &ltdiv class="col-8"&gt
                                                &ltselect name="rating" class="form-select" required aria-label="ratingSelect"&gt
                                                    &ltoption selected value=""&gt&lt/option&gt
                                                    &ltoption value="1"&gt1&lt/option&gt
                                                    &ltoption value="2"&gt2&lt/option&gt
                                                    &ltoption value="3"&gt3&lt/option&gt
                                                    &ltoption value="4"&gt4&lt/option&gt
                                                    &ltoption value="5"&gt5&lt/option&gt
                                                    &ltoption value="6"&gt6&lt/option&gt
                                                    &ltoption value="7"&gt7&lt/option&gt
                                                    &ltoption value="8"&gt8&lt/option&gt
                                                    &ltoption value="9"&gt9&lt/option&gt
                                                    &ltoption value="10"&gt10&lt/option&gt
                                                &lt/select&gt
                                            &lt/div&gt
                                            &ltdiv class="col-4"&gt
                                                &ltdiv class="text-end"&gt
                                                    &ltbutton type="submit" class="btn btn-primary float-right"&gtСохранить&lt/button&gt
                                                &lt/div&gt
                                            &lt/div&gt
                                        &lt/div&gt
                                &lt/div&gt
                                &ltdiv class="modal-footer"&gt
                                    &ltdiv class="container-fluid"&gt
                                        {% for review in reviews|get_item:conf.id %}
                                            &ltbr&gt
                                            &ltdiv class="row"&gt
                                              &ltdiv class="card" style="width: 100%;"&gt
                                                &ltdiv class="card-body"&gt
                                                    &lth5 class="card-title"&gt{{ review.author }}&lt/h5&gt
                                                    &ltp class="card-text"&gt{{ review.text }}&lt/p&gt
                                                    &lthr /&gt
                                                    &lti&gt&ltp class="card-text"&gtДата конференции: {{ conference_dates|get_item:conf.id }}&lt/p&gt&lt/i&gt
                                                    &ltb&gt&ltp class="card-text"&gt
                                                        &ltspan style="font-size:115%;color:gold;"&gt&starf;&lt/span&gt
                                                        {{ review.rating}}&lt/p&gt&lt/b&gt
                                                &lt/div&gt
                                              &lt/div&gt
                                            &lt/div&gt
                                        {% endfor %}
                                    &lt/div&gt
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
