## Представления

### Представление для регистрации нового пользователя
``` py
def registration(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/races')

    else:
        form = CreateUserForm()

    return render(request, 'registration.html', {'form': form})
```
В зависимости от метода запроса возвращает форму регистрации
или регистрирует нового пользователя в бд по введеным в форме данным.

### Представление для авторизации пользователя
```py
def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request=request, username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                return HttpResponse('Invalid login')
            else:
                login(request, user)
                return redirect('/races')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
```
В зависимости от метода запроса возвращает форму авторизации
или авторизовывает пользователя по введеным в форме данным.

### Представление для получения данных о конкретном пользователе
```py
def get_user(request, user_id):
    try:
        user_object = User.objects.get(pk=user_id)

    except User.DoesNotExist:
        raise Http404("User does not exist")

    if user_object.is_racer:
        racer_object = Racer.objects.get(user_id=user_id)
        isRacerBool = True
        isRacer = 'User is racer'
        racerInfo = f'Racer class: {racer_object.drive_class} | Racer experience: {racer_object.experience} years'
        racerDesc = f'{racer_object.description}'

    else:
        isRacerBool = False
        isRacer = 'User is not racer'
        racerInfo = ''
        racerDesc = f''

    return render(request, 'userPage.html',
                  {'user': user_object, 'racerInfo': racerInfo, 'racerDesc': racerDesc, 'isRacer': isRacer,
                   'isRacerBool': isRacerBool})
```
Вовзращает форму с данными о пользователе, полученными по id этого пользователя.

### Представление для получения списка гонок
```py
def get_races(request):
    races_object = Race.objects.all()
    winners = []
    for race_object in races_object:
        if race_object.winner_id:
            winners.append(race_object.winner_id.team)

        else:
            winners.append('No winner')

    races_and_winners = dict(zip(races_object, winners))
    return render(request, "races.html", {'dataset': races_and_winners})
```
Вовзращает форму с таблицей данных о всех гонках, так же с возможностью выбора конкретной гонки.

### Представление для получения данных о конкретной гонке
```py
def get_race(request, race_id):
    winners = []
    try:
        race_object = Race.objects.get(pk=race_id)
        if race_object.status == 'over':
            # winners_team = race_object.winner_id.team
            winners = list(Racer.objects.filter(team=race_object.winner_id.team))

        racers_stats = list(Statistic.objects.filter(race_id=race_id))
        comments_list = Comment.objects.filter(race_id=race_id)

    except User.DoesNotExist:
        raise Http404("Data does not exist")

    try:
        user = User.objects.get(id=request.user.id)
        if request.user.is_authenticated and user.is_racer:
            racer_and_not_start = (user.is_racer and race_object.status == "not started")
            reg = (Statistic.objects.filter(user_id=Racer.objects.get(user_id=request.user))
                   & Statistic.objects.filter(race_id=race_id))
            racer_and_not_start = (racer_and_not_start and not reg)

        else:
            racer_and_not_start = False
    except:
        racer_and_not_start = False

    try:
        user = User.objects.get(id=request.user.id)
        if request.user.is_authenticated and user.is_racer:
            racer_not_start_reg = (user.is_racer and race_object.status == "not started")
            reg = (Statistic.objects.filter(user_id=Racer.objects.get(user_id=request.user))
                   & Statistic.objects.filter(race_id=race_id))
            racer_not_start_reg = (racer_not_start_reg and reg)

        else:
            racer_not_start_reg = False
    except:
        racer_not_start_reg = False

    return render(request, 'race.html', {'race': race_object, 'rns': racer_and_not_start,
                                         'rnsr': racer_not_start_reg, 'racers': racers_stats,
                                         'winners': winners, 'comments': comments_list})
```
Вовзращает форму данными о конкретной гонке по ее id.
Так же, на этой форме, участики могут зарегистрироваться или отменить регистрацию на гонку.
И все авторизованные пользователи могут читать и оставлять комментарии.

### Представление для регистрации пользователя как гонщика
```py
def racer_registration(request):
    form = RacerReg(request.POST or None)
    if request.method == 'POST':
        # form = RacerReg(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            racer = Racer(
                user_id=request.user,
                description=cleaned_data['description'],
                experience=cleaned_data['experience'],
                drive_class=cleaned_data['drive_class'],
                team=cleaned_data['team']
            )

            user = User.objects.get(pk=request.user.id)
            user.is_racer = True
            user.save()
            racer.save()
            return redirect(f'/users/{request.user.id}')

    return render(request, 'racerReg.html', {'form': form})
```
В зависимости от метода запроса возвращает форму регистрации нового гонщика
или регистрирует пользователя в бд как гонщика.

### Представление для регистрации гонщиков на гонку
```py
def register_for_race(request, race_id):
    race_object = Race.objects.get(pk=race_id)
    if race_object.winner_id is not None:
        return redirect('/races')

    if not request.user.is_authenticated:
        return redirect('/races')

    user = User.objects.get(pk=request.user.id)
    racer = Racer.objects.get(user_id=user)
    stats = Statistic.objects.filter(race_id=race_object) & Statistic.objects.filter(user_id=racer)
    if stats.count() > 0:
        return redirect('/races')

    stats = Statistic.objects.create(user_id=racer, race_id=race_object)
    return redirect('/races/' + str(race_object.id))
``` 
Представление регистрирует авторизованного гонщика как участника выбранной гонки.

### Представление для удаления регистрации гонщиков на гонку
```py
def unregister_for_race(request, race_id):
    race_object = Race.objects.get(pk=race_id)
    if race_object.winner_id is not None:
        return redirect('/races')

    if not request.user.is_authenticated:
        return redirect('/races')

    user = User.objects.get(pk=request.user.id)
    racer = Racer.objects.get(user_id=user)
    stats = Statistic.objects.filter(race_id=race_object) & Statistic.objects.filter(user_id=racer)
    if stats.count() <= 0:
        return redirect('/races')

    stats.delete()
    return redirect('/races/' + str(race_object.id))
```
Представление противоположное предыдущему.
Удаляет регистрацию авторизованного гонщика из выбранной гонки.

### Представление для создания новых комментариев
```py
def commentCreate(request, race_id):
    form = CommentCreate(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            race = Race.objects.get(pk=race_id)
            user = User.objects.get(pk=request.user.id)
            comment = Comment(
                main_text=cleaned_data['main_text'],
                race_id=race,
                race_date=race.race_date,
                type=cleaned_data['type'],
                rate=random.randint(1, 10),
                commentator_id=user
            )
            comment.save()
            return redirect(f'/races/{race_id}')

    return render(request, 'comment.html', {'form': form})
```
В зависимости от метода запроса возвращает форму для написания нового комментария к гонке
или создает новый комментарий к гонке в бд.