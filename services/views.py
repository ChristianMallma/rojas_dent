from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    services_obj = Service.objects.all()
    return render(request, "services/services.html", {"services": services_obj})
