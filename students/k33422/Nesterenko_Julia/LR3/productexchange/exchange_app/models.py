import datetime
import pytz

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    """
    Пользователь
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'role', 'manufacturer', 'broker']
    role_types = (
        ('b', 'broker'),
        ('m', 'manufacturer'),
        ('e', 'exchange-admin'),
    )
    role = models.CharField(max_length=1, choices=role_types, default='e')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,
                                     related_name='manufacturer_account',
                                     blank=True, null=True)
    broker = models.ForeignKey('Broker', on_delete=models.CASCADE,
                               related_name='broker_account',
                               blank=True, null=True)

    def __str__(self):
        return self.username


class Manufacturer(models.Model):
    """
    Производитель
    """
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    ceo = models.CharField(max_length=120)
    establishment_date = models.DateField()

    def __str__(self):
        return str(self.pk) + ' - ' + self.name


class ProductType(models.Model):
    """
    Вид товара
    """
    units_types = (
       ('pc', 'pieces'),
       ('kg', 'kilograms'),
       ('gr', 'grams'),
       ('li', 'liters'),
       ('ml', 'milliliters'),
    )
    name = models.CharField(max_length=120)
    units = models.CharField(max_length=2, choices=units_types)
    days_valid = models.PositiveIntegerField()

    def __str__(self):
        return str(self.pk) + ' - ' + self.name


class Product(models.Model):
    """
    Товар
    """
    type = models.ForeignKey('ProductType', on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.DO_NOTHING)
    size = models.PositiveIntegerField(blank=True, null=True, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=30, validators=[MinValueValidator(0)])
    amount = models.PositiveIntegerField()
    manufacturing_date = models.DateTimeField()

    @property
    def expiration_date(self):
        return self.manufacturing_date + datetime.timedelta(self.type.days_valid)

    def __str__(self):
        return (str(self.id) + ' | ' + str(self.manufacturer) + ' | '
                + str(self.type) + ' | ' + str(self.manufacturing_date))


class Broker(models.Model):
    """
    Брокер
    """
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    telephone = models.CharField(max_length=12)
    company = models.CharField(max_length=120)

    @property
    def average_salary(self):
        today = datetime.datetime.now(pytz.utc)
        consignments = Consignment.objects.filter(broker=self, status='s')
        if consignments:
            first_date = min(consignments.values('opening_date'))["opening_date"]
            workmonths = (today - first_date).days // 30
            workmonths = workmonths if workmonths != 0 else 1
        return float(sum([c.total_price for c in consignments]))*0.1 // workmonths

    def __str__(self):
        return str(self.id) + ' - ' + str(self.first_name) + ' ' + str(self.last_name)


class Consignment(models.Model):
    """
    Партия
    """
    status_types = (
       ('a', 'active'),
       ('c', 'cancelled'),
       ('s', 'signed'),
    )
    terms_types = (
        ('pp', 'prepay'),
        ('ap', 'afterpay'),
    )
    status = models.CharField(max_length=1, choices=status_types, default='a', blank=True)
    terms = models.CharField(max_length=2, choices=terms_types)
    opening_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    broker = models.ForeignKey('Broker', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField('Product', through='ProductInConsignment', blank=True)

    @property
    def total_price(self):
        order_parts = ProductInConsignment.objects.filter(consignment=self)
        return sum([pc.product.price*pc.amount for pc in order_parts])

    def __str__(self):
        return str(self.id) + ' - ' + str(self.broker) + ' - ' + str(self.opening_date)


class ProductInConsignment(models.Model):
    """
    Товар в партии
    """
    consignment = models.ForeignKey('Consignment', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

