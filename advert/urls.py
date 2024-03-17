from django.urls import path
from . import views

app_name = 'advert'

urlpatterns = [
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('create_advertisement/', views.create_advertisement, name='create_advertisement'),
    # Add URL patterns for other views as needed
]