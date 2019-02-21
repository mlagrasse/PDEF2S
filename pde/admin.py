from django.contrib import admin
from .models import PDE

# Register your models here.


class PDEAdmin(admin.ModelAdmin):
    list_display = ['user', 'machine', 'ip',  'cat', 'exe']
    search_fields = (
        'ip', 'user'
    )


admin.site.register(PDE, PDEAdmin)