from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(models.Model):
    """
    This model implements a User objects to request loans.
    """
    GENDER_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]

    document_number = models.CharField(_('DNI'),
                                       max_length=15)

    first_name = models.CharField(_('Nombre'),
                                  max_length=50)

    last_name = models.CharField(_('Apellido'),
                                 max_length=50)

    gender = models.CharField(_('Género'),
                              choices=GENDER_CHOICES,
                              max_length=50)

    email = models.EmailField()

    amount = models.IntegerField(_('Monto'))
