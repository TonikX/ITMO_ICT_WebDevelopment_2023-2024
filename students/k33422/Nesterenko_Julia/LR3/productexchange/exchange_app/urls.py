from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('manufacturer/', ManufacturerListAPIView.as_view()),
   path('manufacturer/create/', ManufacturerCreateAPIView.as_view()),
   path('manufacturer/<int:pk>/', ManufacturerOneAPIView.as_view()),
   path('manufacturer/<int:pk>/delete', ManufacturerDeleteAPIView.as_view()),
   path('manufacturer/<int:pk>/edit', ManufacturerEditAPIView.as_view()),

   path('producttype/', ProductTypeListAPIView.as_view()),
   path('producttype/create/', ProductTypeCreateAPIView.as_view()),
   path('producttype/<int:pk>/', ProductTypeOneAPIView.as_view()),
   path('producttype/<int:pk>/delete', ProductTypeDeleteAPIView.as_view()),
   path('producttype/<int:pk>/edit', ProductTypeEditAPIView.as_view()),

   path('broker/', BrokerListAPIView.as_view()),
   path('broker/create/', BrokerCreateAPIView.as_view()),
   path('broker/<int:pk>/', BrokerOneAPIView.as_view()),
   path('broker/<int:pk>/delete', BrokerDeleteAPIView.as_view()),
   path('broker/<int:pk>/edit', BrokerEditAPIView.as_view()),

   path('product/', ProductListAPIView.as_view()),
   path('product/create/', ProductCreateAPIView.as_view()),
   path('product/<int:pk>/', ProductOneAPIView.as_view()),
   path('product/<int:pk>/delete', ProductDeleteAPIView.as_view()),
   path('product/<int:pk>/edit', ProductEditAPIView.as_view()),

   path('consignment/', ConsignmentListAPIView.as_view()),
   path('consignment/create/', ConsignmentCreateAPIView.as_view()),
   path('consignment/<int:pk>/', ConsignmentOneAPIView.as_view()),
   path('consignment/<int:pk>/delete', ConsignmentDeleteAPIView.as_view()),
   path('consignment/<int:pk>/edit', ConsignmentEditAPIView.as_view()),

   path('productinconsignment/', ProductInConsignmentListAPIView.as_view()),
   path('productinconsignment/create/', ProductInConsignmentCreateAPIView.as_view()),
   path('productinconsignment/<int:pk>/', ProductInConsignmentOneAPIView.as_view()),
   path('productinconsignment/<int:pk>/delete', ProductInConsignmentDeleteAPIView.as_view()),
   path('productinconsignment/<int:pk>/edit', ProductInConsignmentEditAPIView.as_view()),

   path('productsbytypeanddate/', ProductsByTypeAndDateAPIView.as_view()),
   path('topmanufacturerbydate/', TopManufacturerByDateAPIView.as_view()),
   path('productsnotsoldbycompany/', ProductsNotSoldByCompanyAPIView.as_view()),
   path('expiredproducts/', ExpiredProductsAPIView.as_view()),
   path('brokersalarybycompany/', BrokerSalaryByCompanyAPIView.as_view()),
   ]
