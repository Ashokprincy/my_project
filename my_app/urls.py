from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "My App Admin"
admin.site.site_title = "My App"
admin.site.index_title = "Welcome to My App Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
