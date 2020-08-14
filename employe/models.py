from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    # user = models.ForeignKey(User)
    emp_id = models.IntegerField(unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emp_address =  models.CharField(max_length=255)
    emp_sal =  models.FloatField()

    class Meta:
        ordering = ['-firstname','-lastname']

    def __str__(self):
        return self.firstname

