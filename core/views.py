from django.shortcuts import render
from .models import Testimonial


# Create your views here.
def home(request):
    testimonial_objs = Testimonial.objects.all()
    return render(request, "core/home.html", {"testimonial_objs": testimonial_objs})


# def blog(request):
#     return render(request, "core/../clinical_cases/templates/clinical_cases/projects.html")
