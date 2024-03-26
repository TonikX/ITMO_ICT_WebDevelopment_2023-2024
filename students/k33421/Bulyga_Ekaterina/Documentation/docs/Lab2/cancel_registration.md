<h1>Представление cancel_registration</h1>
<p>Функция для отмены регистрации на конференцию.</p>
<pre>
<code>
def cancel_registration(request):
    print('cancel')
    if request.method == 'POST':
        conf_id = request.POST['conf_id']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        conf.user_registered.remove(user)
        Performance.objects.filter(conference=conf, user=user).delete()
    return redirect('/my_registrations')
</code>
</pre>