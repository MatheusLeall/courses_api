from django.contrib import admin
from django.urls import path, include
from courses.urls import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="School courses API",
      default_version='v1',
      description="A simple course API to practice Django REST Framework and Swagger integration",
      terms_of_service="https://www.dicionarioinformal.com.br/termos.php",
      contact=openapi.Contact(email="contact@school.com"),
      license=openapi.License(name="Individual License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('courses.urls')),
    path('api/v2/', include(router.urls)),
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
