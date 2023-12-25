from django.urls import path
from .views import write_text, images

urlpatterns = [
    path('', write_text, name='write_text'),
    path('images/', images, name="images")
]

