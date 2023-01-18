from django.db import models

class Banderas(models.Model):
    imagen=models.CharField(max_length=25)

    def __str__(self):
        return self.imagen
