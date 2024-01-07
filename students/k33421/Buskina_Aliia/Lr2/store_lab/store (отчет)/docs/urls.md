### Также для оптимизации файл urls.py был разделен для каждого приложения, чтобы не было перенагрузки 

### urls.py (общий файл проекта)
```python
"""
URL configuration for store_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', include('main.urls')),
    path('basket/', include('basket.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### urls.py (для приложения order)
```python
from django.urls import path

from .views import start_order

urlpatterns = [
    path('start_order/', start_order, name='start_order'),
]
```

### urls.py (для приложения basket)
```python
from django.urls import path
from basket.views import add_basket, basket, checkout, hx_basket_menu, update_basket, hx_basket_total

urlpatterns = [

    path('', basket, name='basket'),
    path('checkout/', checkout, name='checkout'),
    path('hx_basket_menu/', hx_basket_menu, name='hx_basket_menu'),
    path('hx_basket_total/', hx_basket_total, name='hx_basket_total'),
    path('update_basket/<int:product_id>/<str:action>/', update_basket, name='update_basket'),
    path('add_basket/<int:product_id>/', add_basket, name='add_basket'),

]

```

### urls.py (для приложения main)
```python
from django.urls import path
from main.views import frontpage, signup, store, mypage, mypage_edit
from django.contrib.auth import views
from products.views import product
urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('mypage/', mypage, name='mypage'),
    path('mypage/edit/', mypage_edit, name='mypage_edit'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('store/', store, name='store'),
    path('store/<slug:slug>/', product, name='product'),
     ]
```