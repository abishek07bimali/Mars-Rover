
from django.contrib import admin
from django.urls import path, include
from MarsRober import settings
from django.conf.urls.static import static  # Add this line for importing static

admin.site.site_header = "Django Project"
admin.site.site_title = "First Django Project"
admin.site.index_title = "Welcome to my first Django project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)