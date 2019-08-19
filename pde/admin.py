from django.contrib import admin
from .models import PDE

# Register your models here.


class PDEAdmin(admin.ModelAdmin):
    list_display = ['user', 'source_ip', 'destination_ip',  'source_mac', 'destination_mac', 'hash', 'api', 'pde']
    search_fields = (
        'ip', 'user'
    )


admin.site.register(PDE, PDEAdmin)
