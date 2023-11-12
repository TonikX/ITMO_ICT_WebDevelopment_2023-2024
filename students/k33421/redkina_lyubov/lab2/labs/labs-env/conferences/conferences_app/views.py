from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Author, Conference, Registration, Presentation, Review
from .forms import AuthorForm, RegistrationForm, PresentationForm, ReviewForm


def home(request):
    return render(request, 'home.html', {})

def all_authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = '/'

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'edit_author.html'
    success_url = '/'




def all_registrations(request):
    registrations_list = Registration.objects.all()
    return render(request, 'registrations.html', {'registrations': registrations_list})

def registration_detail(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)
    return render(request, 'registration_detail.html', {'registration': registration})

class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'add_registration.html'
    success_url = '/'

class RegistrationUpdateView(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'edit_registration.html'
    success_url = '/'

class RegistrationDeleteView(DeleteView):
    model = Registration
    template_name = 'delete_registration.html'
    success_url = '/'




def all_reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews_list})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = '/'

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'edit_review.html'
    success_url = '/'




def all_presentations(request):
    presentations_list = Presentation.objects.all()
    return render(request, 'presentations.html', {'presentations': presentations_list})

def presentation_detail(request, presentation_id):
    presentation = get_object_or_404(Presentation, pk=presentation_id)
    return render(request, 'presentation_detail.html', {'presentation': presentation})

class PresentationCreateView(CreateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'add_presentation.html'
    success_url = '/'

class PresentationUpdateView(UpdateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'edit_presentation.html'
    success_url = '/'




def all_conferences(request):
    conferences_list = Conference.objects.all()
    return render(request, 'conferences.html', {'conferences': conferences_list})

def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    return render(request, 'conference_detail.html', {'conference': conference})

def conference_authors(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    # Получаем все регистрации для данной конференции
    registrations = Registration.objects.filter(conference=conference)
    # Формируем словарь, где ключи - конференции, значения - списки авторов
    authors_by_conference = {}
    for registration in registrations:
        if registration.conference not in authors_by_conference:
            authors_by_conference[registration.conference] = []
        authors_by_conference[registration.conference].append({'author': registration.author, 'title': registration.title})
    return render(request, 'conference_authors.html', {'authors_by_conference': authors_by_conference})
