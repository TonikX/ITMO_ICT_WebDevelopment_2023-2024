from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
import datetime


class Guest(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_photos', default='profile_photos/user.svg')
    country = models.CharField(max_length=64, default='Russia')
    about_info = models.TextField(default="A very interesting person")

    def __str__(self) -> str:
        return f'{self.last_name} {str(self.first_name)}'

    class Meta:
        ordering = ['id']
    
    @property
    def reservations(self):
        return Reservation.objects.filter(guest=self)
    
    @property
    def reviews(self):
        return Review.objects.filter(guest=self)


class Hotel(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    about_info = models.TextField()
    thumbnail = models.ImageField(upload_to='hotel_photos', null=True)

    def __str__(self) -> str:
        return f'{self.name} ({str(self.country)}, {str(self.city)})'

    class Meta:
        ordering = ['id']

    @property
    def rooms(self):
        return Room.objects.filter(hotel=self)
    
    @property
    def guests(self):
        last_month_guests = []
        for room in self.rooms:
            last_month_guests.extend(room.get_last_month_guests())
        return list(set(last_month_guests))


class Room(models.Model):
    ECONOMY = 'EC'
    STANDARD = 'ST'
    JUNIOR_SUITE = 'JS'
    SUITE = 'SU'

    ROOM_TYPE = (
        (ECONOMY, 'Economy'),
        (STANDARD, 'Standard'),
        (JUNIOR_SUITE, 'Junior Suite'),
        (SUITE, 'Suite'),
        )
    
    BATHROOM = 'BR'
    WI_FI = 'WF'
    AIR_CONDITIONER = 'AC'
    FRIDGE = 'FR'
    JACUZZI = 'JC'
    WASHING_MACHINE = 'WM'
    PARKING = 'PA'
    SWIMMING_POOL = 'SP'
    MINI_BAR = 'MB'
    BREAKFAST = 'BF'
    ALL_IN = 'AI'

    COMMODITIES_LIST = (
        (BATHROOM, 'Bathroom'),
        (WI_FI, 'Wi-Fi'),
        (AIR_CONDITIONER, 'Air conditioner'),
        (FRIDGE, 'Fridge'),
        (JACUZZI, 'Jacuzzi'),
        (WASHING_MACHINE, 'Washing machine'),
        (PARKING, 'Parking'),
        (SWIMMING_POOL, 'Swimming pool'),
        (MINI_BAR, 'Mini bar'),
        (BREAKFAST, 'Breakfast'),
        (ALL_IN, 'All in'),
    )
    
    
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(max_length=2, choices=ROOM_TYPE, default=ECONOMY)
    capacity = models.PositiveSmallIntegerField(validators=(MinValueValidator(1), MaxValueValidator(10)))
    thumbnail = models.ImageField(upload_to='room_photos', null=True)
    commodities = MultiSelectField(choices=COMMODITIES_LIST, max_choices=11, max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return f'{self.hotel} - {str(self.get_type_display())} (for {str(self.capacity)})'

    class Meta:
        ordering = ['id']

    @property
    def reviews(self):
        reservations = Reservation.objects.filter(room=self)
        return Review.objects.filter(reservation__in=reservations)

    def get_last_month_guests(self):
        ending_date = datetime.date.today()
        start_date = ending_date - datetime.timedelta(days=30)
        reservations = Reservation.objects.filter(room=self, end_date__range=[start_date, ending_date])
        return [res.guest for res in reservations]
    
    def available(self, start, end):
        reservations = (Reservation.objects.filter(room=self, status='AC') |
                    Reservation.objects.filter(room=self, status='AW'))
        for res in reservations:
            print(type(res.start_date))
            if ((start <= res.start_date and end >= res.end_date) or
                    (res.start_date <= start <= res.end_date) or
                    (res.start_date <= end <= res.end_date) or
                    (end <= start)):
                return False
        return True
    


class Reservation(models.Model):
    ACTIVE = 'AC'
    AWAITS = 'AW'
    FINISHED = 'FI'
    CANCELLED = 'CA'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (AWAITS, 'Awaits'),
        (FINISHED, 'Finished'),
        (CANCELLED, 'Cancelled'),
    )

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default='AW')

    def __str__(self) -> str:
        return f'{str(self.status)} - {self.guest} booked {str(self.room)} for {str(self.start_date)} - {str(self.end_date)}'

    class Meta:
        ordering = ['id']

    @property
    def review(self):
        return Review.objects.filter(reservation=self)

    @property
    def full_price(self):
        days = (self.end_date - self.start_date).days
        days = days if days != 0 else 1
        return self.room.price * days



class Review(models.Model):
    RATING_CHOICE = (
        ('1', '★☆☆☆☆☆☆☆☆☆'),
        ('2', '★★☆☆☆☆☆☆☆☆'),
        ('3', '★★★☆☆☆☆☆☆☆'),
        ('4', '★★★★☆☆☆☆☆☆'),
        ('5', '★★★★★☆☆☆☆☆'),
        ('6', '★★★★★★☆☆☆☆'),
        ('7', '★★★★★★★☆☆☆'),
        ('8', '★★★★★★★★☆☆'),
        ('9', '★★★★★★★★★☆'),
        ('10', '★★★★★★★★★★'),
    )

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    rating = models.CharField(choices=RATING_CHOICE)
    body = models.TextField()

    def __str__(self) -> str:
        return f'{self.date} - {str(self.rating)} (about {str(self.reservation.room)} by {str(self.reservation.guest)})'

    class Meta:
        ordering = ['id']