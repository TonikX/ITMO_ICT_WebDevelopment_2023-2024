from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register('get-info', views.ActionViewSet, basename='info')

router.register('animals', views.AnimalViewSet)
router.register('animals/winterp-laces', views.WinterPlaceViewSet)

router.register('food', views.TypeOfDietViewSet)
router.register('food/diets', views.DietViewSet)
router.register('habitats', views.HabitatViewSet)

router.register('locations', views.AreaViewSet)
router.register('locations/aviaries', views.AviaryViewSet)
router.register('locations/who-is-there', views.AnimalInAviaryViewSet)


router.register('other-zoos', views.ZooViewSet)
router.register('ownings', views.OwningViewSet)


urlpatterns = router.urls
