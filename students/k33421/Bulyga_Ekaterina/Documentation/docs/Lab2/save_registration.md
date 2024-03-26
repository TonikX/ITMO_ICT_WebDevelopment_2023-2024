<h1>Представление save_registration</h1>
<p>Функция для сохранения регистрации пользователя на конференцию.</p>
<pre>
<code>
def save_registration(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        conf_id = request.POST['conf_id']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        conf.user_registered.add(user)
        Performance.objects.create(conference=conf, user=user, topic=topic)
    return redirect('/')
</code>
</pre>