## Админ-панель
Через данную админ-панель можно создавать пользователей, категории, продукты и отмечать оплаченные заказы 
```python title="admin.py"
from django.contrib import admin
from .models import Category, Product, User
from order.models import Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
```
