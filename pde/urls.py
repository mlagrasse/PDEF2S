"""Example URL configuration."""

from django.conf.urls import url
from django.http import HttpResponse
from . import views


from .views import add, index

urlpatterns = [
    url(r'^$', views.index, name='pde'),
    url(r'^details/(?P<user>\w+)$', views.details, name='user'),
    url(r'^add/$', views.add, name='add'),
    url(r'files/(?P<path>.*)$', views.serve),

]
