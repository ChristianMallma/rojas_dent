from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Nombre", 'name': 'name', 'type': "text", 'id': "name-1"}
    ), min_length=2, max_length=100)
    email = forms.EmailField(label='Correo', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': "Correo", 'name': 'email', 'type': "email", 'id': "email-1"}
    ), min_length=5, max_length=100)
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': "Mensaje", 'name': 'content', 'rows': "6", 'id': "content-1"}
    ), min_length=10, max_length=1000)
