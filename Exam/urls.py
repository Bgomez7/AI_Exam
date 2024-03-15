from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Map '/' to the home view function
]
