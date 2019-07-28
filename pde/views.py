
from django.shortcuts import render
from django.template.defaultfilters import register
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .models import PDE
from rest_framework.decorators import api_view
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.conf import settings
from django_otp.decorators import otp_required
from django.dispatch import receiver
from two_factor.signals import user_verified
from django.contrib.sites.shortcuts import get_current_site

import hashlib
# Create your views here.

import os
import magic
from django.conf import settings

from django.http import Http404, HttpResponse
from django.views.generic import View

from django_encrypted_filefield.crypt import Cryptographer

@login_required
def index(request):

    dis = PDE.objects.order_by('user').values_list('user', flat=True).distinct()
    admin = request.user.is_staff
    username = request.user.get_username()
    context = {
        # 'pde': data,
        'dfi': request.user,
        'dis': dis,
        'admin': admin,
        'username': username,
        'len': len(dis)
    }
    return render(request, 'pde/index.html', context)


@login_required
def details(request, user):
    username = request.user.get_username()
    admin = request.user.is_staff
    data = []
    if user == username or admin:
        data = PDE.objects.filter(user=user).order_by('date')[::-1]

    context = {
        'dfi': request.user,
        'pde': data,
        'user': user,
        'admin': admin,
        'username': username,
        'len': len(data)
    }
    return render(request, 'pde/details.html', context)


@otp_required
def serve(request, path):
    response = FileResponse(open(settings.MEDIA_ROOT+'\\pde\\files\\'+path, 'rb'))
    return response


@register.filter(name='trim')
def trim(value):
    return value.split('\\')[-1]


@api_view(['POST', ])
def add(request):
    """Endpoints for listing and retrieving PDE."""
    parser_classes = (FileUploadParser,)
    ip = strip_tags(request.POST.get("ip", False))
    machine = strip_tags(request.POST.get("machine", False))
    user = strip_tags(request.POST.get("user", False))
    cat = float(strip_tags(request.POST.get("cat", False)))
    exe = strip_tags(request.POST.get("exe", False))
    pde = request.FILES.get('pde', False)
    key = request.META.get('HTTP_AUTHORIZATION', False).split(" ")[-1]
    response = {"status": 'Error'}
    test = ""
    if ip and machine and user and cat and exe and pde:
        n = PDE.objects.create(ip=ip, machine=machine, user=user, cat=cat, exe=exe, pde=pde, hash=test, api=key)
        response = {"status": 'Success'}
        file = request.FILES.get('pde', False)
        md5 = hashlib.md5()
        file.seek(0)
        while True:
            buf = file.read(104857600)
            if not buf:
                break
            md5.update(buf)
        md5 = md5.hexdigest()
        file.seek(0)
        n.hash = md5
        n.save()
    permission_classes = (HasAPIKey,)
    return Response(response)


@receiver(user_verified)
def test_receiver(request, user, device, **kwargs):
    current_site = get_current_site(request)
    if device.name == 'backup':
        message = 'Hi %(username)s,\n\n'\
                  'You\'ve verified yourself using a backup device '\
                  'on %(site_name)s. If this wasn\'t you, your '\
                  'account might have been compromised. You need to '\
                  'change your password at once, check your backup '\
                  'phone numbers and generate new backup tokens.'\
                  % {'username': user.get_username(),
                     'site_name': current_site.name}
        user.email_user(subject='Backup token used', message=message)


@otp_required
@login_required
def get(request, path):
    print(path)
    with open(os.path.join(os.path.join(settings.MEDIA_ROOT, 'pde/files'), path), "rb") as f:
        content = f.read()

    content = Cryptographer.decrypted(content)

    return HttpResponse(
        content, content_type=magic.Magic(mime=True).from_buffer(content))
    # response = FileResponse(open(settings.MEDIA_ROOT+'\\pde\\files\\'+path, 'rb'))
    # return response


#
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django_encrypted_filefield.views import FetchView
#
#
# class MyPermissionRequiredMixin(LoginRequiredMixin):
#     """
#     Your own rules live here
#     """
#     pass
#
#
# class MyFetchView(MyPermissionRequiredMixin, FetchView):
#     pass
