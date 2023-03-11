from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    in_time = models.DateTimeField(blank=True,null=True)
    out_time = models.DateTimeField(blank=True,null=True)
    current_status = models.BooleanField(default=False)
    money = models.IntegerField(blank=True,null=True,default=False)
    def __str__(self):
        return self.first_name+self.last_name
    

class AttendanceLogs(models.Model):
    in_time = models.DateTimeField(blank=True,null=True)
    out_time = models.DateTimeField(blank=True,null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()

    
