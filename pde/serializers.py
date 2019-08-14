"""Example serializers."""

from rest_framework import serializers

from .models import PDE
from PDEF2S import settings


class PDESerializer(serializers.ModelSerializer):
    pde_url = serializers.SerializerMethodField()

    def get_pde_url(self, obj):
        return '%s%s' % (settings.SITE_URL, obj.pde)

    class Meta:
        model = PDE
        fields = ('ip', 'machine', 'user', 'date', 'cat', 'exe', 'pde_url' )


