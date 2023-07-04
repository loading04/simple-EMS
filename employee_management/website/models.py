from django.db import models
from django_enumfield import enum
# Create your models here.


class status(enum.Enum):
    available = 0
    not_available = 1
    days_off = 2
    


class emp(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField(null=False)
    position = models.CharField(max_length=255,default="")
    status = enum.EnumField(status , default=status.available)
    date_return = models.DateField(blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")   