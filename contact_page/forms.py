from django import forms
from .models import Message


class MessageForm(forms.Form):
    message_nick = forms.CharField(max_length=64)
    message_email = forms.EmailField()
    message_content = forms.CharField()
    message_date = forms.DateTimeField(auto_now_add=True)

