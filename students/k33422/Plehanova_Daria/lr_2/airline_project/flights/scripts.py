from . import models
from datetime import timedelta
from django.utils import timezone


def create_tickets_for_flights():
    flights = models.Flight.objects.all()

    for flight in flights:
        seat_configuration = flight.airplane.seat_configuration

        for seat_class, config in seat_configuration.items():
            rows = config['rows']
            layout = config['layout']

            for row in range(1, rows + 1):
                for seat in layout:
                    seat_number = f"{row}{seat}"
                    Ticket.objects.create(
                        flight=flight,
                        seat_class=seat_class,
                        seat=seat_number
                    )


SEAT_PRICES = {
    'economy': 6000.00,
    'business': 18000.00
}


def set_ticket_prices():
    tickets = models.Ticket.objects.all()

    for ticket in tickets:
        ticket.price = SEAT_PRICES[ticket.seat_class]
        ticket.save()


def update_flight_statuses():
    current_time = timezone.now()

    flights = models.Flight.objects.filter(status__in=['scheduled', 'boarding', 'in-flight', 'landed'])

    for flight in flights:
        # Если время вылета еще не наступило
        if flight.departure_time > current_time:
            continue
        # Если до вылета осталось менее 30 минут
        elif flight.departure_time <= current_time < flight.departure_time + timedelta(minutes=30):
            flight.status = 'boarding'
        # Если рейс в пути
        elif flight.departure_time <= current_time < flight.arrival_time:
            flight.status = 'in-flight'
        # Если рейс приземлился, но еще не завершен
        elif flight.arrival_time <= current_time < flight.arrival_time + timedelta(minutes=30):
            flight.status = 'landed'
        # Если рейс завершен
        else:
            flight.status = 'completed'
        flight.save()
