from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django_cryptography.fields import encrypt
from django_encrypted_filefield.fields import EncryptedFileField


class PDE(models.Model):
    pde = encrypt(EncryptedFileField(upload_to='pde/files/', max_length=None))
    ip = models.CharField(max_length=16)
    machine = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    cat = models.FloatField(null=True, blank=True, default=None)
    exe = models.CharField(max_length=512)
    hash = models.CharField(max_length=256, default=None, blank=True)
    api = models.CharField(max_length=256, default="N/A", blank=True)

    def __str__(self):
        return self.user + " " + self.ip

    class Meta:
            verbose_name_plural = "PDE"

