from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Kitoblar API",
      default_version='v1',
      description="API dokumentatsiyasi",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,), # Bu yerda AllowAny bo'lishi muhim
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')), # Ilova urls.py faylini ulash
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]