from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register('products', viewset=views.ProductViewSet)
router.register('products-by-companies', viewset=views.ProductByCompanyViewSet)
router.register('companies', viewset=views.CompanyViewSet)
router.register('broker-companies', viewset=views.BrokerCompanyViewSet)
router.register('brokers', viewset=views.BrokerViewSet)
router.register('consignments', viewset=views.ConsignmentViewSet)
router.register(r'brokers-with-company', views.BrokerCompanyViewSet, basename='brokers-with-company')

urlpatterns = router.urls
