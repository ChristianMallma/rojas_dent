from django.shortcuts import render, get_object_or_404
from .models import Page


# Create your views here.
def page(request, keyword):
    page_object = get_object_or_404(Page, keyword=keyword)
    return render(request, 'pages/sample.html', {'page': page_object})
