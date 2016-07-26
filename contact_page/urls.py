from django.conf.urls import url
from .views import HomePageView

urlpatterns = [
    url(r'^contact/$', HomePageView.as_view()),
]