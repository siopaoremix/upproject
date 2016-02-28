from django.db import models

# Create your models here.
class Results(models.Model):
    class Meta:
        permissions = (('can_view_admin' , 'Can view admin page'),)