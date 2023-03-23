from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

MONEY_CHOICES = (
    ("credit", "credit"),
    ("debit", "debit"),
    
)
class Staff(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='staff',
        to_field = 'username',
        default="admin"
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    in_time = models.DateTimeField(blank=True,null=True)
    out_time = models.DateTimeField(blank=True,null=True)
    current_status = models.BooleanField(default=False)
    money = models.IntegerField(blank=True,null=True,default=False)
    def __str__(self):
        return self.first_name+self.last_name
    

class AttendanceLogs(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='attendance_logs',
        to_field = 'username',
        default="admin"
    )
    in_time = models.DateTimeField(blank=True,null=True)
    out_time = models.DateTimeField(blank=True,null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()


class MoneyLogs(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='money_logs',
        to_field = 'username',
        default="admin"
    )
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False,null=False)
    type = models.CharField(max_length=9,
                  choices=MONEY_CHOICES,
                  default="")
    time = models.DateTimeField()
    details = models.CharField(max_length=100,default="",null=True)
    
    # def __str__(self):
    #     return self.staff.first_name + " " + str(self.amount)
