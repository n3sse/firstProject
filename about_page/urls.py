from django.conf.urls import url
from .views import HomePageView

urlpatterns = [
    url(r'^about/$', HomePageView.as_view()),
]
