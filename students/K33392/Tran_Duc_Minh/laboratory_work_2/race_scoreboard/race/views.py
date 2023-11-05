from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Team, Participant, Race, Commentator, Comment, RaceRegistration, RaceResult
from django.contrib.auth.forms import AuthenticationForm
from .forms import RaceRegistrationForm, CommentForm


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Đăng nhập người dùng
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Chuyển hướng sau khi đăng nhập
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def register_user(request):
    if request.method == 'POST':
        # Xử lý đăng ký người dùng mới
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('home')  # Chuyển hướng người dùng sau khi đăng ký

    return render(request, 'registration/register.html')

def race_list(request):
    current_date = timezone.now().date()
    races = Race.objects.filter(race_date__gte=current_date)
    user = request.user
    register_race = Race.objects.filter(participant__user=user)
    return render(request, 'races/race_list.html', {'races': races, 'register_race': register_race})
@login_required
def view_race(request, race_id):
    comment_sent = False
    race = get_object_or_404(Race, id=race_id)
    participants = RaceRegistration.objects.filter(race=race)

    # Kiểm tra xem người dùng đã đăng ký vào cuộc đua hiện tại hay chưa
    participant = Participant.objects.filter(user=request.user, registered_races=race).first()

    # Xử lý biểu mẫu đăng ký
    form = RaceRegistrationForm(request.POST or None)  # Tạo một thể hiện của biểu mẫu

    # Xử lý biểu mẫu Comment
    comment_form = CommentForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            if not participant:
                # Nếu người dùng chưa đăng ký, tạo đăng ký mới
                team_name = form.cleaned_data.get('team_name')
                car_description = form.cleaned_data.get('car_description')
                experience = form.cleaned_data.get('experience')
                rank = form.cleaned_data.get('rank')

                # Tạo thể hiện Team nếu chưa tồn tại
                team, created = Team.objects.get_or_create(name=team_name)

                participant = Participant.objects.create(
                    user=request.user,
                    team=team,
                    car_description=car_description,
                    experience=experience,
                )
                RaceRegistration.objects.create(race=race, participant=participant)  # Đăng ký vào cuộc đua

        elif comment_form.is_valid():
            print("hãy comment")
            commentator, created = Commentator.objects.get_or_create(user=request.user)
            comment = comment_form.save(commit=False)
            comment.race = race
            comment.commentator = commentator
            comment.save()

            comment_form = CommentForm()

            comment_sent = True

    # Hiển thị ô viết comment nếu đã đăng ký cuộc đua
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

@login_required
def race_result_list(request):
    all_results = RaceResult.objects.all()
    unique_results = {}

    for result in all_results:
        race_id = result.race.id
        if race_id not in unique_results:
            unique_results[race_id] = result

    unique_results = list(unique_results.values())

    return render(request, 'races/race_result_list.html', {'race_results': unique_results})

@login_required
def race_result_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    race_results = RaceResult.objects.filter(race=race)
    return render(request, 'races/race_result_detail.html', {'race': race, 'race_results': race_results})

@login_required
def unregister_from_race(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    participant = Participant.objects.filter(user=request.user, registered_races=race).first()

    if participant:
        # Remove the user's registration from the race
        RaceRegistration.objects.filter(race=race, participant=participant).delete()

    return redirect('view_race', race_id=race.id)

@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})