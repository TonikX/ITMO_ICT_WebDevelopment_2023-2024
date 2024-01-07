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
