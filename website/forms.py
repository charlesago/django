from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    title = forms.CharField(label="Votre titre", required=True)
    content = forms.CharField(label="Votre contenu", required=True)

    class Meta:
        model = Message
        fields = ["title", "content"]