from django.db import models
from django_enumfield import enum
# Create your models here.


class status(enum.Enum):
    available = 0
    not_available = 1
    days_off = 2
    

class employee(models.Model):
    full_name = models.CharField(max_length=255)
    date_birth = models.DateField(null=True)
    position = models.CharField(max_length=255,default="")
    status = enum.EnumField(status , default=status.available)
    date_return = models.DateField(null=True)
    email = models.EmailField(default="")
    phone = models.CharField(default="")
    