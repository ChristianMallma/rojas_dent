from django.urls import path
from . import views

urlpatterns = [
    # Services paths
    path('', views.services, name="services"),
]
