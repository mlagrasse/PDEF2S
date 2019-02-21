from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class PDE(models.Model):
    pde = models.FileField(max_length=None)
    ip = models.CharField(max_length=16)
    machine = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    cat = models.FloatField()
    exe = models.CharField(max_length=255)

    def __str__(self):
        return self.user + " " + self.ip

    class Meta:
            verbose_name_plural = "PDE"

