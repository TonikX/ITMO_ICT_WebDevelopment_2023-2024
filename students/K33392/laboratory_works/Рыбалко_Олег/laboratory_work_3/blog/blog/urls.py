from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
    title="API for a blog website",
    default_version="v1",
    description="It has all features needed to implement a blog website",
    license=openapi.License(name="MIT"),
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  path("admin/", admin.site.urls),
  path("api/", include("blog_app.urls")),
  path("auth/", include("djoser.urls")),
  path("auth/", include("djoser.urls.authtoken")),
  re_path(
    r"^profile_pics/(?P<path>.*)$",
    serve,
    {
      "document_root": "profile_pics/",
    },
  ),
  path(
    "swagger/",
    schema_view.with_ui("swagger", cache_timeout=0),
    name="schema-swagger-ui",
  ),
]
