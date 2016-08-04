from django.views.generic import CreateView
from .models import Message


class NewMessageView(CreateView):
    model = Message
    fields = ['message_nick', 'message_email', 'message_content']
    template_name = "contact_page/index.html"
    success_url = '/'

