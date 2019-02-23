from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import viewsets
from .models import PDE
from rest_framework.decorators import api_view
from .serializers import PDESerializer
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.conf import settings
from django_otp.decorators import otp_required
# Create your views here.

@login_required
def index(request):

    dis = PDE.objects.order_by('user').values_list('user', flat=True).distinct()
    admin = request.user.is_staff
    context = {
        # 'pde': data,
        'dis': dis,
        'admin': admin
    }
    return render(request, 'pde/index.html', context)

@login_required
def details(request, user):
    data = PDE.objects.filter(user=user).order_by('date')[::-1]
    admin = request.user.is_staff
    context = {
        'pde': data,
        'user': user,
        'admin': admin
    }
    return render(request, 'pde/details.html', context)


@otp_required
def serve(request, path):
    response = FileResponse(open(settings.MEDIA_ROOT+'\\pde\\files\\'+path, 'rb'))
    return response


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

    response = {"status": 'Error'}
    if ip and machine and user and cat and exe and pde:
        new = PDE.objects.create(ip=ip, machine=machine, user=user, cat=cat, exe=exe, pde=pde)
        response = {"status": 'Success'}
    permission_classes = (HasAPIKey,)
    return Response(response)
