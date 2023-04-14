from django.db import models

# Create your models here
class Supplier(models.Model):
    id=models.AutoField(primary_key=True)
    supplier_first_name=models.CharField(max_length=25)
    supplier_middle_name=models.CharField(max_length=25)
    supplier_last_name=models.CharField(max_length=25)
    supplier_address=models.CharField(max_length=25)
    supplier_aphone1=models.CharField(max_length=25)
    supplier_aphone2=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.supplier_first_name
    