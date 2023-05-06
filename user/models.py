from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length = 30)

    class Meta:
        db_table = 'user_tb'


    

