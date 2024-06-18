from django import forms
from .models import Kontakt

class KontaktForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Navn',}), required=True)
    melding = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Melding',}), required=True)

    class Meta:
        model = Kontakt
        fields = ('sender', 'melding')
