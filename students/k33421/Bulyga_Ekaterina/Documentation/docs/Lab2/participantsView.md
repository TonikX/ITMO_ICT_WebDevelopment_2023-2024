<h1>Представление participants</h1>
<p>Представление данных об участниках конкретной конференции.</p>
<pre>
<code>
def participants(request):
    participants_dict = {}
    conference_list = Conference.objects.all()
    for conference in conference_list:
        performances = Performance.objects.filter(conference=conference)
        participants_list = []
        print(conference.user_registered)
        for performance in performances:
            participants_list.append(str(performance.user))
        participants_dict[conference.name] = participants_list
    print(participants_dict)
    return render(request, 'conferences/participants_table.html', {'participants': participants_dict})
</code>
</pre>