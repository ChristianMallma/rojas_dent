from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request, keyword):
    if keyword != 'all':
        services_obj = Service.objects.filter(group=keyword)
    else:
        services_obj = Service.objects.all()

    return render(request, "services/services.html", {"services": services_obj})
