from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('admin/', include('adminRole.urls')),
    path('user/', include('userRole.urls')),
]
