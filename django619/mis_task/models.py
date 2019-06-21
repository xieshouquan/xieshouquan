from django.db import models

# Create your models here.

class Mis_task(models.Model):
    task_id=models.IntegerField(primary_key=True)
    task_name=models.CharField(max_length=50)
    patrol_circuit=models.CharField(max_length=50)
    Inspector=models.CharField(max_length=30)
    enabled_state=models.CharField(max_length=20)
    Initial_pole_number=models.CharField(max_length=50)
    termination_pole_number=models.CharField(max_length=50)
    sender=models.CharField(max_length=20)
    departure_time=models.DateTimeField(auto_now_add=True)
    remarks=models.CharField(max_length=100)
    class Meta:
        db_table="mis_task"