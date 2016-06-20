from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>[0-9]+)/$', views.codeView, name="codeView")
]