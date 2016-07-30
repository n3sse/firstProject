from django.conf.urls import url
from .views import HomePageView

urlpatterns = [
    url(r'^authors/$', HomePageView.as_view()),
]
