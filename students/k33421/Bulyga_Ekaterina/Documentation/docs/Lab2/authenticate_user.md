<h1>Представление authenticate_user</h1>
<p>Функция для авторизации пользователя.</p>
<pre>
<code>
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Вы успешно авторизованы!")
    else:
        messages.success(request, "Неверная связка логин + пароль")
</code>
</pre>