<h1>Представление my_registrations</h1>
<p>Представление данных о регистрации на конференции для конкретного пользователя.</p>
<pre>
<code>
def my_registrations(request):
    conference_to_topic = {}
    user = User.objects.get(username=str(request.user))
    conf_user_registered = Conference.objects.filter(user_registered=user)
    for conference in conf_user_registered:
        performance = Performance.objects.filter(user=user, conference=conference)
        if performance:
            conference_to_topic[conference] = str(performance.get())
    return render(request, 'conferences/my_registrations.html', {'conference_to_topic': conference_to_topic})
</code>
</pre>