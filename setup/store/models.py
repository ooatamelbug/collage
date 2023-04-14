from django.db import models

# Create your models here.

class Store(models.Model):
    id=models.AutoField(primary_key=True)
    store_name=models.CharField(max_length=30)
    store_reg_no=models.CharField(max_length=30)
    store_location=models.CharField(max_length=30)
    store_phone1=models.CharField(max_length=30)
    store_phone2=models.CharField(max_length=30, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.store_name