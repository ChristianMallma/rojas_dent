from django.urls import path
from . import views

urlpatterns = [
    # clinical_cases paths
    path('', views.clinical_cases, name="clinical_cases"),
]
