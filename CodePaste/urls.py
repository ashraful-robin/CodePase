from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^$', include('paste.urls')),
    url(r'^$', 'paste.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
]
