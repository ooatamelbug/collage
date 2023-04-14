from django.db import models
from uuid import uuid4
from users.models import User 

# Create your models here.

class Responsibilities(models.Model):
    id=models.AutoField(primary_key=True)
    resp_name=models.CharField(max_length=15)
    resp_type=models.CharField(max_length=3)
    resp_action= models.CharField(max_length=3)
    resp_status= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resp_name
    


class UserResponsibilities(models.Model):
    id=models.AutoField(primary_key=True)
    user_id= models.ForeignKey(User,related_name='user_responsibilities', on_delete=models.CASCADE)
    resp_id= models.ForeignKey(Responsibilities, related_name= 'responsibilities_user', on_delete=models.CASCADE)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)

    def __str__(self):
        return self.user_id
