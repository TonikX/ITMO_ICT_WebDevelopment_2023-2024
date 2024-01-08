from django.urls import path, include
from django.contrib import admin
from product import views
urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/favorite/', views.ProductDetail.as_view()),
     # URL-шаблон для избранных книг
#path('api/v1/favorite-products/', views.FavoriteProductsList.as_view(), name='favorite_products'),

    # URL-шаблон для переключения состояния избранного продукта
#path('api/v1/products/<int:product_id>/toggle-favorite/', views.ToggleFavoriteBookView.as_view(), name='toggle_favorite_product'),
]