from django.shortcuts import render
from .models import ClinicalCases, ClinicalCasesDetail


# Create your views here.
def clinical_cases(request, keyword):
    if keyword != 'all':
        clinical_cases_obj = ClinicalCases.objects.filter(service=keyword)
    else:
        clinical_cases_obj = ClinicalCases.objects.all()

    return render(request, "clinical_cases/projects.html", {"clinical_cases_obj": clinical_cases_obj})


def clinical_cases_detail(request, keyword):
    if keyword != 'all':
        clinical_cases_detail_obj = ClinicalCasesDetail.objects.filter(clinical_case=keyword)
    else:
        clinical_cases_detail_obj = ClinicalCasesDetail.objects.all()

    return render(request, "clinical_cases/clinical_cases_detail.html", {"clinical_cases_detail_obj": clinical_cases_detail_obj})
