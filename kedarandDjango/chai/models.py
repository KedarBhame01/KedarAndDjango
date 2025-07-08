from django.db import models
from django.utils import timezone
# Create your models here.
class ChaiVariety(models.Model):
    Chai_Type_Choice =[('ML','Masala'),('GR','Ginger'),('PL','Plain')]
    name = models.CharField(max_length= 100)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices = Chai_Type_Choice)