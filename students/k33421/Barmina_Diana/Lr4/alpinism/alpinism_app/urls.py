from django.urls import path, include, re_path
from rest_framework import routers
#from drf_yasg import openapi
#from drf_yasg.views import get_schema_view
from .views import *
from rest_framework import permissions

app_name = "alpinism_app"

router = routers.DefaultRouter()
#router.register('participatings', ParticipationAPIView, basename='participating')
# define the router path and viewset to be used
'''schema_view = get_schema_view(
   openapi.Info(
      title="Alpinism API",
      default_version='v1.0.0',
      description=""
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)'''


urlpatterns = [
    # no
    path('alpinists/', AlpinistsAPIView.as_view(), name='alpinists'),

    # yes
    path('climbings/', ClimbingsListView.as_view(), name='climbings'),
    # yes
    path('climbings/<int:pk>/', ClimbingsDetailView.as_view(), name='climbing-detail'),

    # yes
    path('mountains/', MountainsListView.as_view(), name='mountains'),
    # не надо - вся информация спокойно умещается в карточках
    path('mountains/<int:pk>/', MountainsDetailView.as_view(), name='mountain-detail'),

    # no - не уверена, что надо
    path('participatings/', ParticipationAPIView.as_view({'get': 'list'}), name='participatings'),
    # no - сделано как отображение участников на странице восхождения
    path('userpage/participatings/<int:pk>/', ParticipatingDetailView.as_view(), name='users-participation-detail'),
    # yes
    path('userpage/<int:user_id>/climbings-participation/<int:pk>/create/', ParticipatingCreateView.as_view(), name='users-participation-create'),
    # no
    path('userpage/participatings/<int:pk>/update/', ParticipatingUpdateView.as_view(), name='users-participating-update'),
    # yes
    path('userpage/participatings/<int:pk>/delete/', ParticipatingDeleteView.as_view(), name='users-participating-delete'),

    # yes
    path('clubs/', ClubsListView.as_view(), name='clubs'),
    # yes
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),

    # скорее всего не надо
    path('club-memberships/', ClubMemberViewSet.as_view({'get': 'list'}), name='club-memberships'),
    # yes
    path('userpage/<int:pk>/club-membership/create/', ClubMembershipCreateView.as_view(), name='users-club-membership-create'),
    # yes
    path('userpage/club-membership/<int:pk>/delete/', ClubMembershipDeleteView.as_view(), name='users-club-membership-delete'),

    # no
    path('emergency/', EmergencyListView.as_view(), name='emergency-list'),

    #re_path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('mountains/<int:pk>/', MountainDetailView.as_view()),
    # path('mountain/<int:pk>/climbings', ClimbMountainView.as_view()),
    # path('club-memberships/', ClubMemberViewSet.as_view({'post': 'list'})),
    # path('', include(router.urls)),
    # path('participatings/create/', ParticipatingForClimbingCreateView.as_view()),
    # path('club-membership/your-membership/', ClubMembershipCreateView.as_view()),
    # path('club-membership/your-membership/', ClubMembershipCreateView.as_view()),
    # path('climbings/<int:pk>/create-participation/', ParticipatingForClimbingCreateView.as_view()),

]