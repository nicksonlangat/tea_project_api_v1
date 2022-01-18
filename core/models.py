from operator import mod
from django.db import models

from accounts.models import Employee

# Create your models here.
class TeaWeight(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    entry_date = models.DateField()
    weight = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self) -> str:
        return self.employee.first_name