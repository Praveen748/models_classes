from django.db import models

# Create your models here.
class Country(models.Model):
    Country_id=models.CharField(max_length=100,primary_key=True)
    Country_name=models.CharField(max_length=100,unique=True)


class Capital(models.Model):
    Country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    Capital_name=models.CharField(max_length=100 ,unique=True)
    