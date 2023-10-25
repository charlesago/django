from django.forms import ModelForm, Textarea
from django import forms
from website.models import Message, User, Category, Response


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'category']
        widgets = {
            "content": Textarea(attrs={"cols": 30, "rows": 4})

        }
    category = forms.ModelChoiceField(queryset=Category.objects.all())


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['content']
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']