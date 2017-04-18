from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Employee(User):
    #User表的扩展
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)