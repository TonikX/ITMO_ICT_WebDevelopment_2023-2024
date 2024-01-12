Представления(с комментариями в коде):

    # Импорты модулей Django
    from django.shortcuts import render, redirect
    from django.http import HttpResponseForbidden
    from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView
    from django.contrib.auth.views import LoginView, LogoutView
    from django.contrib.auth import login, authenticate
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.contrib.auth.models import User
    
    # Импорт моделей и форм из приложения
    from .models import Hotel, Reservation, Room, Comment
    from .forms import RegisterForm
    
    # Главная страница
    def main_page(request):
        return render(request, 'main_page.html')
    
    # Регистрация гостей
    def registerPage(request):
        form = RegisterForm
    
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    
        context = {'form': form}
        return render(request, 'register_guests.html', context)
    
    # Вход в аккаунт
    def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                return redirect('/main/')
    
        context = {}
        return render(request, 'login.html', context)
    
    # Выход из аккаунта
    class Logout(LogoutView):
        template_name = 'logout.html'
    
    # Просмотр всех номеров
    class RoomsList(ListView):
        model = Room
        template_name = 'list_rooms.html'
    
    # Бронирование
    class BookingCreateView(LoginRequiredMixin, CreateView):
        model = Reservation
        fields = ['room', 'arrival_date', 'departure_date']
        template_name = 'create_reservation.html'
        success_url = '/users_bookings'
    
        def form_valid(self, form):
            form.instance.guest = self.request.user
            return super(BookingCreateView, self).form_valid(form)
    
    # Просмотр бронирований пользователя
    def user_book(request):
        need_book = Reservation.objects.filter(guest=request.user)
        current_book = {"object_list": need_book}
        return render(request, 'users_bookings.html', current_book)
    
    # Редактирование брони
    class UpdateBooking(UpdateView):
        model = Reservation
        fields = ['room', 'arrival_date', 'departure_date']
        template_name = 'update_book.html'
        success_url = '/users_bookings/'
    
    # Удаление брони
    class DeleteBooking(LoginRequiredMixin, DeleteView):
        model = Reservation
        template_name = 'del_book.html'
        success_url = '/users_bookings/'
    
        def delete(self, request, *args, **kwargs):
            # Разрешить удаление только создателю бронирования
            if self.get_object().guest == request.user:
                return super(DeleteBooking, self).delete(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You can't cancel this booking")
    
    # Написать комментарий
    class CommentCreateView(LoginRequiredMixin, CreateView):
        model = Comment
        fields = ['reservation', 'text', 'rate']
        template_name = 'create_comment.html'
        success_url = '/all_comments/'
    
        def form_valid(self, form):
            form.instance.guest = User.objects.get(username=self.request.user.username)
            return super(CommentCreateView, self).form_valid(form)
    
    # Посмотреть все комментарии
    def all_comments(request):
        list_comments = {"object_list": Comment.objects.all()}
        return render(request, 'all_comments.html', list_comments)
    
    # Получить список гостей в отелях
    def guests_list(request):
        guest_in_hotel = Reservation.objects.all()
        list_of_guests = {"object_list": guest_in_hotel}
        return render(request, 'guests.html', list_of_guests)


