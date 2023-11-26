# Django Views

## `home`

- **Description:** Renders the 'home.html' template.
- **HTTP Method:** GET.
```python
def home(request):
    return render(request, 'home.html')
```

## `login_view`

- **Description:** Handles user login. If the form is submitted with valid credentials, it logs in the user and redirects to the 'home' view.
- **HTTP Methods:** GET, POST.
```python
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # User login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect after login
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
```
## `register_user`

- **Description:** Handles user registration. If the form is submitted with valid data, it creates a new user and logs them in, then redirects to the 'home' view.
- **HTTP Methods:** GET, POST.
```python
def register_user(request):
    if request.method == 'POST':
        # Handle new user registration
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        # Redirect users after registration
        return redirect('home')  

    return render(request, 'registration/register.html')
```
## `race_list`

- **Description:** Lists races, filtering for races occurring in the future and displaying races the current user has registered for.
- **HTTP Method:** GET.
```python
def race_list(request):
    current_date = timezone.now().date()
    races = Race.objects.filter(race_date__gte=current_date)
    user = request.user
    register_race = Race.objects.filter(participant__user=user)
    return render(request, 'races/race_list.html', {'races': races, 'register_race': register_race})
```
## `view_race`

- **Description:** Displays race details and handles race registration and comment submission. It also checks if the user is registered for the race and, if so, allows them to comment.
- **HTTP Methods:** GET, POST.
```python
def view_race(request, race_id):
    comment_sent = False
    race = get_object_or_404(Race, id=race_id)
    participants = RaceRegistration.objects.filter(race=race)

    # Check if the user is registered to the current race
    participant = Participant.objects.filter(user=request.user, registered_races=race).first()

    # Process the registration form
    form = RaceRegistrationForm(request.POST or None) 

    # Handle the Comment form
    comment_form = CommentForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            if not participant:
                # If the user is not registered, create a new registration
                team_name = form.cleaned_data.get('team_name')
                car_description = form.cleaned_data.get('car_description')
                experience = form.cleaned_data.get('experience')
                rank = form.cleaned_data.get('rank')

                # Create a Team instance if it doesn't exist yet
                team, created = Team.objects.get_or_create(name=team_name)

                participant = Participant.objects.create(
                    user=request.user,
                    team=team,
                    car_description=car_description,
                    experience=experience,
                )
                # Sign up for the race
                RaceRegistration.objects.create(race=race, participant=participant)  

        elif comment_form.is_valid():
            print("hãy comment")
            commentator, created = Commentator.objects.get_or_create(user=request.user)
            comment = comment_form.save(commit=False)
            comment.race = race
            comment.commentator = commentator
            comment.save()

            comment_form = CommentForm()

            comment_sent = True

    # Show the comment box if you have registered for the race
    can_comment = participant is not None

    return render(request, 'races/race_detail.html',
                  {'race': race,
                   'participants': participants,
                   'can_comment': can_comment,
                   'form': form,
                   'comment_form': comment_form,
                   'comment_sent': comment_sent
                   }
                  )
```
## `race_result_list`

- **Description:** Lists race results.
- **HTTP Method:** GET.
```python
def race_result_list(request):
    all_results = RaceResult.objects.all()
    unique_results = {}

    for result in all_results:
        race_id = result.race.id
        if race_id not in unique_results:
            unique_results[race_id] = result

    unique_results = list(unique_results.values())

    return render(request, 'races/race_result_list.html', {'race_results': unique_results})
```

## `race_result_detail`

- **Description:** Displays detailed race results for a specific race.
- **HTTP Method:** GET.
```python
def race_result_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    race_results = RaceResult.objects.filter(race=race)
    return render(request, 'races/race_result_detail.html', {'race': race, 'race_results': race_results})

```

## `unregister_from_race`

- **Description:** Handles user's race unregistration. If the user is registered for the race, it removes their registration and redirects to the 'view_race' view.
- **HTTP Method:** GET.
```python
def unregister_from_race(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    participant = Participant.objects.filter(user=request.user, registered_races=race).first()

    if participant:
        # Remove the user's registration from the race
        RaceRegistration.objects.filter(race=race, participant=participant).delete()

    return redirect('view_race', race_id=race.id)
```
