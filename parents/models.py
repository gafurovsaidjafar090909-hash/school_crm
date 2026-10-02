from django.db import models
from accounts.models import User


class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="parent_profile",null=True,blank=True )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


