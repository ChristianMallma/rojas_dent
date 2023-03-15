from django.urls import path
from . import views

urlpatterns = [
    # clinical_cases paths
    path('<str:keyword>/', views.clinical_cases, name="clinical_cases"),
]
