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