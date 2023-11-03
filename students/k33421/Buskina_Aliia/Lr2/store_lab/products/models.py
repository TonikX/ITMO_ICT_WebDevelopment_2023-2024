from django.db import models
from django.contrib.auth.models import User

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
