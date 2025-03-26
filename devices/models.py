from django.contrib.auth.models import User
from django.db import models

# Modelo de Dispositivo
class Device(models.Model):
    DEVICE_TYPES = [
        ('tablet', 'Tablet'),
        ('smartphone', 'Smartphone'),
        ('keyboard', 'Keyboard'),
        ('pen', 'Pen'),
        ('pos', 'POS')
    ]
    MODELS = [
        ('TL10', 'TL10'),
        ('TL12', 'TL12'),
        ('T307G', 'T307G'),
        ('T307F', 'T307F')
    ]
    ODMS = [
        ('ZTECH', 'ZTECH'),
        ('EPUDO', 'EPUDO'),
        ('HENA', 'HENA')
    ]

    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    model = models.CharField(max_length=20, choices=MODELS)
    device_id = models.CharField(max_length=50, unique=True)
    odm = models.CharField(max_length=20, choices=ODMS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.device_type} - {self.model} ({self.device_id})"

# Registrar o modelo no admin
from django.contrib import admin
admin.site.register(Device)
