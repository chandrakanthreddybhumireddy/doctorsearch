# urls.py
# urls.py

# app/urls.py
from django.urls import path
from .views import index, search_doctors
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),  # Assumes you have an 'index' view for your homepage
    path('search_doctors/', search_doctors, name='search_doctors'),
    # Add other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
