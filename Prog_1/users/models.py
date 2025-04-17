from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")

    def __str__(self):
        return self.full_name
