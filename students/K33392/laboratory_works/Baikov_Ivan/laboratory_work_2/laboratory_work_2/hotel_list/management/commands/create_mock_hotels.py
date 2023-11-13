from django.core.management.base import BaseCommand
from hotel_list.models import Hotel

class Command(BaseCommand):
    help = 'Creates mock hotel data'

    def handle(self, *args, **kwargs):
        # Create mock hotels
        hotels = [
            {
                'name': 'Hotel A',
                'owner': 'Owner A',
                'address': '123 Main Street, City A',
                'description': 'A cozy hotel in the heart of City A',
                'room_types': 'Single, Double, Suite',
                'price': 100.00,
                'capacity': 50,
                'amenities': 'Free Wi-Fi, Swimming Pool, Gym',
            },
            {
                'name': 'Hotel B',
                'owner': 'Owner B',
                'address': '456 Elm Street, City B',
                'description': 'Luxury hotel with a view of City B',
                'room_types': 'Deluxe, Executive Suite',
                'price': 200.00,
                'capacity': 30,
                'amenities': 'Spa, Fine Dining, Concierge Service',
            },
            {
                'name': 'Hotel C',
                'owner': 'Owner C',
                'address': '789 Oak Street, City C',
                'description': 'Affordable hotel for budget travelers',
                'room_types': 'Economy, Standard',
                'price': 50.00,
                'capacity': 100,
                'amenities': 'Free Breakfast, Parking',
            },
            # Add more hotels as needed
        ]

        for hotel_data in hotels:
            Hotel.objects.create(**hotel_data)

        self.stdout.write(self.style.SUCCESS('Successfully created mock hotels'))
