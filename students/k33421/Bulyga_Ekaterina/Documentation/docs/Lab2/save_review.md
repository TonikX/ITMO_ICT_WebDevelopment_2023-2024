<h1>Представление save_review</h1>
<p>Функция для сохранения отзыва пользователя на конференцию.</p>
<pre>
<code>
def save_review(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        conf_id = request.POST['conf_id']
        text = request.POST['reviewText']
        user = User.objects.get(username=request.user)
        conf = Conference.objects.get(id=conf_id)
        Review.objects.create(author=user, text=text, conference=conf, rating=rating)
    return redirect('/')
</code>
</pre>