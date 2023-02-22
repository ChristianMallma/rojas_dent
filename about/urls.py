from django.urls import path
from . import views

urlpatterns = [
    # About paths
    path('', views.about, name="about"),
]
