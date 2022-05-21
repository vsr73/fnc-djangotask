from django.db import models

# Create your models here.
class details(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    mobile_num=models.IntegerField(primary_key=True)
    mail=models.EmailField(max_length=250)
    address=models.CharField(max_length=300)
    password=models.CharField(max_length=300)


'''fname=models.CharField(max_length=30,not_null=True)
lname=models.CharField(max_length=30,not_null=True)
mobile_num=models.IntegerField(primary_key=True,not_null=True)
mail=models.EmailField(max_length=250,not_null=True)
address=models.CharField(max_length=300,not_null=True)
password=models.CharField(max_length=300,not_null=True)
'''
