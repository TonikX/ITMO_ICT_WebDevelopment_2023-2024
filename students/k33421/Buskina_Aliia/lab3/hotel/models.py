from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    ROOM_TYPE = (
        ('1', 'single'),
        ('2', 'double'),
        ('3', 'triple'))
    type = models.CharField(max_length=1, choices=ROOM_TYPE)
    price = models.IntegerField()
    floor = models.IntegerField()


    def __str__(self):
        return f'Room №{self.id}'

class Staff(models.Model):
    POSITION_CHOICES = (
        ('hostess', 'Hostess'),
        ('cleaner', 'Cleaner'),
    )

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='cleaner')

    def __str__(self):
        return f'Staff {self.name} {self.surname} - {self.get_position_display()}'

class Guest(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=10, unique=True)
    hometown = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f'Guest {self.name} {self.surname}'


class Cleaning(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_clean = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Cleaning №{self.id} in room № {self.room_id.id} by {self.staff_id.name} {self.staff_id.surname} at {self.date_clean}'


class Checkin(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)

    @property
    def staying_days(self):
        if self.check_in_date and self.check_out_date:
            return (self.check_out_date - self.check_in_date).days
        return None

    @property
    def income(self):
        if self.room_id and self.check_in_date and self.check_out_date:
            room_price = self.room_id.price
            return room_price * self.staying_days
        return None
    def __str__(self):
        return f'Guest {self.guest_id.name} {self.guest_id.surname} lives in room № {self.room_id.id} from {self.check_in_date} till {self.check_out_date}'
