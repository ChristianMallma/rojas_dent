from django.urls import path
from . import views

urlpatterns = [
    # Services paths
    path('<str:keyword>/', views.services, name="services"),
]
