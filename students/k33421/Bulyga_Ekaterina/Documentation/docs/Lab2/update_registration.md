<h1>Представление update_registration</h1>
<p>Функция для обновления регистрации пользователя на конференцию.</p>
<pre>
<code>
def update_registration(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        conf_id = request.POST['conf_id']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        Performance.objects.filter(conference=conf, user=user).update(topic=topic)
    return redirect('/my_registrations')
</code>
</pre>