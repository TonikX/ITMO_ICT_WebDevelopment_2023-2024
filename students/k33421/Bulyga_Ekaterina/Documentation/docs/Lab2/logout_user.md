<h1>Представление authenticate_user</h1>
<p>Функция для выхода из личного кабинета и перенаправления на главную страницу.</p>
<pre>
<code>
def logout_user(request):
    logout(request)
    return redirect('/')
</code>
</pre>