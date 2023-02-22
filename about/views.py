from django.shortcuts import render
from .models import About


# Create your views here.
def about(request):
    # return render(request, "about/about-us.html")
    about_obj = About.objects.all()
    return render(request, "about/about-us.html", {"about_obj": about_obj})
