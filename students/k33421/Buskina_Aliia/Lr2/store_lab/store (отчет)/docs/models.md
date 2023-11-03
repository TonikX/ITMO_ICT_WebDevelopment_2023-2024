## Было создано ряд модолей и классов в разных приложениях, ключевые из которых: категория, продукт, пользователь, отзывы, корзина и заказ

### в приложении product
```python
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    class Meta:
        ordering = ('name','category', 'price')

    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'https://via.placeholder.com/240x240.jpg'

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

### в приложении заказов
```python
from django.db import models

from django.contrib.auth.models import User
from django.db import models

from products.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name='order', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

```

### также был реализован класс корзины
```python
class Basket(object):
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)

        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}

        self.basket = basket

    def __iter__(self):
        for p in self.basket.keys():
            self.basket[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.basket.values():
            item['total_price'] = int(item['product'].price * item['quantity']) / 100

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:
            self.basket[product_id]['quantity'] += int(quantity)

            if self.basket[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_cost(self):
        for p in self.basket.keys():
            self.basket[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.basket.values())) / 100

    def get_item(self, product_id):
        if product_id in self.basket:
            return self.basket[str(product_id)]
        else:
            return None

```

### А также модели заказа
```python
from django.db import models

from django.contrib.auth.models import User
from django.db import models

from products.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name='order', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

```