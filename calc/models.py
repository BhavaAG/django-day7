from django.db import models

# Create your models here.
class Request(models.Model):
    requestid = models.AutoField(db_column = 'req_id',primary_key = True)
    fname = models.CharField(max_length = 25, null = False)
    lname = models.CharField(max_length = 20, null = False)
    dob = models.CharField(max_length = 20, null = False)
    gender = models.CharField(max_length = 10,null = False)
    nationality = models.CharField(max_length = 30, null = False)
    city = models.CharField(max_length = 10, null = False)
    state = models.CharField(max_length = 20, null = False)
    pincode = models.CharField(max_length = 6,null = False)
    qualification = models.CharField(max_length = 10,null = False)
    salary = models.IntegerField(null = False)
    pancard = models.CharField(max_length = 10,null = False)
