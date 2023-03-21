from django.urls import path
from . import views

urlpatterns = [
    # clinical_cases paths
    path('<str:keyword>/', views.clinical_cases, name="clinical_cases"),
    path('detail/<str:keyword>/', views.clinical_cases_detail, name="clinical_cases_detail"),
]
