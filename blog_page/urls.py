from django.conf.urls import url
from .views import ListPosts
urlpatterns = [
    url(r'^$', ListPosts.as_view()),

]
