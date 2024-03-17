from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advert/', include('advert.urls')),
    path('', include('core.urls')),
    path('userauth/', include('userauth.urls')),
    path('payments/', include('payments.urls')),
]
