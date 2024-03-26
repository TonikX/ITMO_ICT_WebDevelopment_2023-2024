<h1>Представление show_conferences</h1>
<p>Представление данных о конференции.</p>
<pre>
<code>
def show_conferences(request):
    conference_list = Conference.objects.all()
    topics = {}
    reviews = {}
    current_user_conf_registered = []
    conference_dates = {}
    for conference in conference_list:
        reviews_list = []
        topics[conference.id] = []
        conf_user_registered = User.objects.filter(conference__id=conference.id)
        for user_registered in conf_user_registered:
            if str(user_registered.username) == str(request.user):
                current_user_conf_registered.append(conference.id)
            performance = Performance.objects.filter(user=user_registered, conference=conference)
            if performance:
                topics.get(conference.id).append('\"' + str(performance.get()) + '\"')
        reviews_query = Review.objects.filter(conference=conference)

        for review in reviews_query:
            reviews_list.append(review)
        reviews[conference.id] = reviews_list
        conference_dates[conference.id] = conference.date
    print(reviews)
    return render(request, 'conferences/conferences.html',
                  {'conferences': conference_list, 'topics': topics, 'registered': current_user_conf_registered,
                   'reviews': reviews, 'conference_dates': conference_dates})
</code>
</pre>