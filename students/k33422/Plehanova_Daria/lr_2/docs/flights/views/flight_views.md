# Контроллеры приложения Flights

## IndexRedirectView

**Маршрут:**  
`url`: reverse_lazy('flights')  

### Описание:
`IndexRedirectView` используется для перенаправления с корневого URL приложения на список полетов.

## FlightListView

**Модель:**  
`model`: models.Flight  
**Шаблон:**  
`template_name`: flights/flight_list.html  

### Описание:
`FlightListView` представляет список всех полетов. Отображает информацию о каждом полете на странице `flight_list.html`.

## FlightDetailView

**Модель:**  
`model`: models.Flight  
**Шаблон:**  
`template_name`: flights/flight_detail.html  

### Описание:
`FlightDetailView` предоставляет детальную информацию о конкретном полете.

## FlightSeatsDetailView

**Модель:**  
`model`: models.Flight  
**Шаблон:**  
`template_name`: flights/flight_seats.html  
**Дополнительный контекст:**  
Получение списка билетов для рейса и их сортировка по классу и месту.

### Описание:
`FlightSeatsDetailView` отображает детальную информацию о местах в конкретном рейсе, включая их статус (забронировано или свободно).

## TicketBookView

**Метод:**  
GET  
**Основное действие:**  
Бронирование билета для конкретного рейса и обновление статуса билета.

### Описание:
`TicketBookView` позволяет пользователю забронировать билет на рейс. Если рейс не запланирован или пользователь уже имеет бронирование для этого рейса, будет вызвано исключение. При успешном бронировании, пользователь перенаправляется на домашнюю страницу.

## ReservationListView

**Модель:**  
`model`: models.Reservation  
**Шаблон:**  
`template_name`: reservation_list.html  

### Описание:
`ReservationListView` отображает список всех бронирований, сделанных текущим пользователем.

## ReservationDeleteView

**Модель:**  
`model`: models.Reservation  
**URL после успешного удаления:**  
`success_url`: reverse_lazy('home')  

### Описание:
`ReservationDeleteView` позволяет пользователю отменить свое бронирование, обновляя статус соответствующего билета.

## ReviewListView

**Модель:**  
`model`: models.Review  
**Шаблон:**  
`template_name`: flights/reviews_list.html  
**Дополнительный контекст:**  
Отображает отзывы, связанные с конкретным рейсом.

### Описание:
`ReviewListView` показывает отзывы, оставленные пользователями для конкретного рейса.

## ReviewCreateView

**Модель:**  
`model`: models.Review  
**Поля для заполнения:**  
`fields`: ['comment', 'rating']  
**Шаблон:**  
`template_name`: flights/review_create.html  

### Описание:
`ReviewCreateView` позволяет авторизованным пользователям, которые ранее совершали рейс, оставить отзыв о нем.

## ReviewUpdateView

**Модель:**  
`model`: models.Review  
**Поля для заполнения:**  
`fields`: ['comment', 'rating']  
**Шаблон:**  
`template_name`: flights/review_update.html  

### Описание:
`ReviewUpdateView` позволяет автору отзыва вносить изменения в свой ранее оставленный отзыв.

## ReviewDeleteView

**Модель:**  
`model`: models.Review  

### Описание:
`ReviewDeleteView` дает возможность автору отзыва удалить свой отзыв.
