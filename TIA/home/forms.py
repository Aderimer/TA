from django import forms
from .models import Kontakt

class KontaktForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Navn',}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email',}), required=True)
    melding = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Melding',}), required=True)

    class Meta:
        model = Kontakt
        fields = ('email', 'sender', 'melding',)
        labels = {'email':"lab_mail", 'sender':"lab_sender", 'melding':"lab_melding",}
