"""Example URL configuration."""

from django.conf.urls import url
from django.http import HttpResponse
from . import views
from django_encrypted_filefield.constants import FETCH_URL_NAME
from django_encrypted_filefield.views import FetchView

from .views import add, index

urlpatterns = [
    url(r'^$', views.index, name='pde'),
    url(r'^details/(?P<user>\w+)$', views.details, name='user'),
    url(r'^add/$', views.add, name='add'),
    # url(r'files/(?P<path>.*)$', views.serve),
    url(
        r"^files/(?P<path>.+)",  # up to you, but path is required
        views.get, name='get'  # your view, your permissions

    ),

]
