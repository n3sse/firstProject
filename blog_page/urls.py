from django.conf.urls import url
from .views import BlogPageView
urlpatterns = [
    url(r'^$', BlogPageView.as_view()),

]
