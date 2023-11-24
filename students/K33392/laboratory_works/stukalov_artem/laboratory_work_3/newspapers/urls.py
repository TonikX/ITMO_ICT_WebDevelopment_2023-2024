from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include, re_path


router = SimpleRouter()
# Базовые эндпоинты для прямого взаимодействия с модельками
router.register(r"newspapers", viewset=views.NewspaperViewSet)
router.register(r"printingOffices", viewset=views.PrintingOfficeViewSet)
router.register(r"postOffices", viewset=views.PostOfficeViewSet)
router.register(r"newspaperEditions", viewset=views.NewspaperEditionViewSet)
router.register(r"newspaperOrders", viewset=views.NewspaperOrderViewSet)
router.register(r"newspaperDistributions", viewset=views.NewspaperDistributionViewSet)

# Специфичные эндпоинты для узконаправленных задач

urlpatterns = [
    path(
        "printingAddressesByName/",
        views.find_printing_addresses_by_name,
    ),
    path(
        "mostPrintedAuthor/",
        views.most_printed_author,
    ),
    path(
        "distributionAddressesByPrice/",
        views.distribution_addresses_by_price,
    ),
    path(
        "lessCountDistributionAddresses/",
        views.less_count_distribution_addresses,
    ),
    path(
        "newspaperDistributionAddresses/",
        views.newspaper_distribution_addresses,
    ),
]

urlpatterns += router.urls
