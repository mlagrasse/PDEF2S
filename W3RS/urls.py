"""W3RS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from two_factor.urls import urlpatterns as tf_urls
from two_factor.admin import AdminSiteOTPRequired
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import LogoutView

admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^settings/', include('django_mfa.urls')),
    url(r'', include(tf_urls)),
    url(r'^pde/', include('pde.urls')),
    url(r'^$', RedirectView.as_view(url='pde/', permanent=False), name='index'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

#
if settings.DEBUG:
    urlpatterns += [
        # url(r'pde/file/(?P<path>.*)$', serve, {
        #     'document_root': settings.MEDIA_ROOT,
        # }),
#         # url(r'^static/(?P<path>.*)$', serve, {
#         #     'document_root': settings.MEDIA_ROOT + "/",
#         # }),
    ]
