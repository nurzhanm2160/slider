from django.urls import path
from .views import get_images

urlpatterns = [
    path('', get_images)
]
