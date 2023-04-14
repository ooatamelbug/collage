from django.db import models
from supplier.models import Supplier
# Create your models here.
class PurchaseOrder(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_desc = models.TextField()
    order_status = models.IntegerField(default=0)
    invoice_number=models.IntegerField()
    invoice_status = models.IntegerField(default=0)
    invoice_atm=models.IntegerField()
    supplier_id=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
