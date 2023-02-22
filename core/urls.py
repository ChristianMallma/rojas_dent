from django.urls import path
from . import views

urlpatterns = [
    # Core paths
    path('', views.home, name="home"),
    # path('blog/', views.blog, name="blog"),
]
