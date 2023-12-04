# Маршруты приложения Flights

В этом разделе представлен краткий обзор маршрутов, используемых в приложении Flights.

## Список маршрутов:

- **Главная страница**  
  **URL Pattern:** `/`  
  **View:** `IndexRedirectView`  
  **Описание:** Перенаправление на список рейсов.


- **Список бронирований**  
  **URL Pattern:** `/reservations/`  
  **View:** `ReservationListView`  
  **Описание:** Просмотр всех бронирований пользователя.


- **Удаление бронирования**  
  **URL Pattern:** `/reservation/<int:pk>/delete/`  
  **View:** `ReservationDeleteView`  
  **Описание:** Удаление конкретного бронирования.


- **Список рейсов**  
  **URL Pattern:** `/flights/`  
  **View:** `FlightListView`  
  **Описание:** Просмотр списка всех рейсов.


- **Детали рейса**  
  **URL Pattern:** `/flights/<int:pk>/`  
  **View:** `FlightDetailView`  
  **Описание:** Просмотр деталей конкретного рейса.


- **Места в рейсе**  
  **URL Pattern:** `/flights/<int:pk>/seats/`  
  **View:** `FlightSeatsDetailView`  
  **Описание:** Просмотр доступных мест в конкретном рейсе.


- **Список отзывов о рейсе**  
  **URL Pattern:** `/flights/<int:pk>/reviews/`  
  **View:** `ReviewListView`  
  **Описание:** Просмотр отзывов о конкретном рейсе.


- **Создание отзыва о рейсе**  
  **URL Pattern:** `/flights/<int:pk>/reviews/create/`  
  **View:** `ReviewCreateView`  
  **Описание:** Создание нового отзыва о рейсе.


- **Редактирование отзыва**  
  **URL Pattern:** `/reviews/<int:pk>/edit/`  
  **View:** `ReviewUpdateView`  
  **Описание:** Редактирование существующего отзыва.


- **Удаление отзыва**  
  **URL Pattern:** `/reviews/<int:pk>/delete/`  
  **View:** `ReviewDeleteView`  
  **Описание:** Удаление отзыва.


- **Бронирование билета**  
  **URL Pattern:** `/ticket/<int:pk>/book/`  
  **View:** `TicketBookView`  
  **Описание:** Бронирование билета на рейс.
