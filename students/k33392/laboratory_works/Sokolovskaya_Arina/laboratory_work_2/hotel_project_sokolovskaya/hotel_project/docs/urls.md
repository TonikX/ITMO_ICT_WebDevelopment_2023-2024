# Urls

    path("main/", main, name='main'),
    path("", main, name='main'),
    path("registration/", register, name='register'),
    path("hotels/", HotelList.as_view(), name='hotels'),
    path("hotel_rooms/<int:hotel_id>", hotel_rooms, name='hotel_rooms'),
    path("book/<int:room_id>", new_book, name='book'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path('login/', auth_views.LoginView.as_view(next_page='main'), name='login'),
    path("my_bookings/", my_bookings, name='my_bookings'),
    path("users_bookings/<str:guest_passport>/", user_book, name='user_book'),
    path("update_book/<int:pk>", UpdateBooking.as_view(), name='update_book'),
    path("delete_book/<int:pk>", DeleteBooking.as_view(), name='delete_book'),
    path("feedback/<int:pk>", new_feedback, name='create_feedback'),
    path('feedback_list/', all_feedbacks, name='feedback_list'),
    path('hotel_guests/<int:hotel_id>', hotel_guests, name="hotel_guests")