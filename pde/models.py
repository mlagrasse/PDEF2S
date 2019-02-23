from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django_cryptography.fields import encrypt


class PDE(models.Model):
    pde = encrypt(models.FileField(upload_to='pde/files/', max_length=None))
    ip = models.CharField(max_length=16)
    machine = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    cat = models.FloatField(null=True, blank=True, default=None)
    exe = models.CharField(max_length=512)

    def __str__(self):
        return self.user + " " + self.ip

    class Meta:
            verbose_name_plural = "PDE"

