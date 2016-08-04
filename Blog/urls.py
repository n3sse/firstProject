from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog_page.urls')),
    url(r'', include('contact_page.urls')),
]
