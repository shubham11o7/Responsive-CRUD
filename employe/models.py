from django.db import models
# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True,auto_created=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emp_address =  models.CharField(max_length=255)
    emp_sal =  models.FloatField()


    def __str__(self):
        return self.firstname

