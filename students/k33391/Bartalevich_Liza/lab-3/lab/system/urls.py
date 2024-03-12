from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('animals', views.AnimalViewSet)
router.register('winter-places', views.WinterPlaceViewSet)

router.register('food', views.TypeOfDietViewSet)
router.register('diets', views.DietViewSet)
router.register('habitats', views.HabitatViewSet)

router.register('locations', views.AreaViewSet)
router.register('aviaries', views.AviaryViewSet)
router.register('who-is-there', views.AnimalInAviaryViewSet)

router.register('other-zoos', views.ZooViewSet)
router.register('ownings', views.OwningViewSet)

urlpatterns = router.urls
