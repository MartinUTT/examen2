from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('api/',include('api.urls')),
    path('',include('home.urls')),
]
