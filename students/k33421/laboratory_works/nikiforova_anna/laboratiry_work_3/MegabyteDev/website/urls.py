from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "website"


schema_view = get_schema_view(
    openapi.Info(
        title="Megabyte API",
        default_version='v1.0.0',
        description=""
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r'whatwedo', RandomWhatWeDoViewSet.as_view({'get': 'list'}), name='whatwedos'),
    path(r'whatwedo/<int:pk>', RandomWhatWeDoViewSet.as_view({'get': 'retrieve'}), name='whatwedo'),

    path(r'rubric', RubricViewSet.as_view({'get': 'list'}), name='rubrics'),
    path(r'rubric/<int:pk>', RubricViewSet.as_view({'get': 'retrieve'}), name='rubric'),

    path(r'hashtag', HashtagViewSet.as_view({'get': 'list'}), name='hashtags'),
    path(r'hashtag/<int:pk>', HashtagViewSet.as_view({'get': 'retrieve'}), name='hashtag'),

    path(r'platform', PlatformViewSet.as_view({'get': 'list'}), name='platforms'),
    path(r'platform/<int:pk>', PlatformViewSet.as_view({'get': 'retrieve'}), name='platform'),

    path(r'article', ArticleViewSet.as_view({'get': 'list'}), name='articles'),
    path(r'article/<int:pk>', ArticleViewSet.as_view({'get': 'retrieve'}), name='article'),

    path(r'banner', BannerViewSet.as_view({'get': 'list'}), name='banners'),
    path(r'banner/<int:pk>', BannerViewSet.as_view({'get': 'retrieve'}), name='banner'),

    path(r'podcast', PodcastViewSet.as_view({'get': 'list'}), name='podcasts'),
    path(r'podcast/<int:pk>', PodcastViewSet.as_view({'get': 'retrieve'}), name='podcast'),

    path(r'podcast/<int:pk>/issues', PodcastIssueViewSet.as_view({'get': 'list'}), name='podcast-issues'),

    path(r'publication', PublicationViewSet.as_view({'get': 'list'}), name='publications'),
    path(r'publication/<int:pk>', PublicationViewSet.as_view({'get': 'retrieve'}), name='publication'),

    path(r'newtone', NewtoneViewSet.as_view({'get': 'list'}), name='newtones'),
    path(r'newtone/<int:pk>', NewtoneViewSet.as_view({'get': 'retrieve'}), name='newtone'),

    path(r'newspaper', NewspaperViewSet.as_view({'get': 'list'}), name='newspaper'),
    path(r'newspaper/<int:pk>', NewspaperViewSet.as_view({'get': 'retrieve'}), name='newspaper'),

    path(r'publication/<int:pk>/pages', PublicationPageViewSet.as_view({'get': 'retrieve'}),
         name='publication-pages'),

    path(r'user/<int:pk>/participated', ParticipantViewSet.as_view({'get': 'list'}),
         name='user-participated'),  # any user can see it
    path(r'user/<int:pk>/favourites', FavouriteViewSet.as_view({'get': 'list'}),
         name='user-favourites'),  # only the registered user can see their own favourites

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
