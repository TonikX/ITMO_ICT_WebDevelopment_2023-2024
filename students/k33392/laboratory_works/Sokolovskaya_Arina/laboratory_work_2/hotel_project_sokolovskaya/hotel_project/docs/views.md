# Views

Регистрация

    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return render(request, 'main.html')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

Бронирование номера

    @login_required
    def new_book(request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        if request.method == 'POST':
            try:
                booking_form = BookingForm(request.POST)
                if booking_form.is_valid():
                    passport = booking_form.cleaned_data['passport']
                if not Guest.objects.filter(passport=passport).exists():
                    Guest.objects.create(
                        user_id=request.user.id,
                        first_name=booking_form.cleaned_data['first_name'],
                        last_name=booking_form.cleaned_data['last_name'],
                        passport=passport)

            tuple1 = booking_form.cleaned_data['check_in_date']
            tuple2 = booking_form.cleaned_data['check_out_date']
            check_in_date = date(tuple1.year, tuple1.month, tuple1.day)
            check_out_date = date(tuple2.year, tuple2.month, tuple2.day)
            duration = (check_out_date - check_in_date).days
            new_booking = Booking(
                room=room,
                hotel=room.hotel,
                guest=Guest.objects.filter(passport=passport).get(),
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                price=duration * room.cost
            )
            Booking.save(new_booking)
            return redirect(request, "user_book", guest_passport=passport)
        except:
            return render(request, 'new_book.html')
    else:
        booking_form = BookingForm()
    return render(request, 'new_book.html', {'form': booking_form})

