from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviar email y redireccionar
            email_object = EmailMessage(
                'Rojas Dent: Nuevo mensaje de contacto',
                f"De {name} <{email}\n\nEscribió:\n\n{content}",
                '',
                ['ruthrojasmanzaneda@gmail.com'],
                reply_to=[email]
            )
            try:
                email_object.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request, "contact/contacts.html", {'form': contact_form})
