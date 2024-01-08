# Регистрация новых пользователей.

###### Модель пользователя

```
class User(AbstractUser):
    description = models.TextField()
    team = models.CharField(max_length=100)
    rating = models.CharField(max_length=15, choices=(('beginner', 'beginner'), ('middle', 'middle'), ('profy', 'profy')))
    car_num = models.CharField(max_length=30)
    car_description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name ='Пользователь'
        verbose_name_plural='Пользователи'
```

###### Модель регистрации

```
class Register(models.Model):
    racer = models.ForeignKey(User, related_name='where_to_drive', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='who_drive', on_delete=models.CASCADE)
    result = models.IntegerField(blank=True, null=True,)
    time_result = models.FloatField(blank=True, null=True,)
    class Meta:
        verbose_name ='Регистация'
        verbose_name_plural='Регистрации'
```

###### Форма регистрации

```
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email",
                  "description", "rating", "team", "car_num", "car_description"]

```

###### Регистрация пользователя

```
def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("user_login")
    else:
        user_form = RegistrationForm()

    return render(request, "register.html", {"user_form": user_form})
```

###### Страница регистрации

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