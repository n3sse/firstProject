from django.conf.urls import url
from .views import HomePageView, BlogPageView, PostDetailView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', PostDetailView.as_view()),
    url(r'^blog/$', BlogPageView.as_view()),
    url(r'^blog/(?P<pk>[0-9]+)/$', PostDetailView.as_view()),
    url(r'^blog/(?P<page>\d+)/$', BlogPageView.as_view()),
]
