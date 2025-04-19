from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(
        verbose_name="Email",
        validators=[EmailValidator()],
        blank=True,
        null=True
    )
    is_admin = models.BooleanField(
        verbose_name="Администратор",
        default=False
    )

    def __str__(self):
        return self.full_name
