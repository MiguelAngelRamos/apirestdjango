from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.name
