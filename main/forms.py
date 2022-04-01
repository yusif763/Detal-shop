from django import forms
from main.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'phone_number'
        )
        widgets = {
            'name':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'adiniz',
                }),
            'phone_number':forms.TextInput(attrs={
                    'class':'form-control py-4',
                     'placeholder':'Nomreniz',
                     'type':'number',
                }),
        }