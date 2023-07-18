from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

class UserDetails(AbstractBaseUser):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    contactno=models.CharField(max_length=12)
    age=models.IntegerField()
    enmarbe=models.IntegerField(null=True)
    enmaraf=models.IntegerField(null=True)
    matmarks=models.IntegerField(null=True)
    gkmarks=models.IntegerField(null=True)
    examtime=models.IntegerField(default=100,null=False)
    mattime=models.IntegerField(default=100,null=False)
    gktime=models.IntegerField(default=100,null=False)
