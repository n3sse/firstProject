from django.conf.urls import url
from .views import NewMessageView

urlpatterns = [
    url(r'contact/$', NewMessageView.as_view()),
]
