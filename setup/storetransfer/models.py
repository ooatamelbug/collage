from django.db import models
from stock.models import StoreStock
from storerequest.models import StoreRequest
from drug.models import Drug

# Create your models here.
class StockTransfer(models.Model):
    id= models.AutoField(primary_key=True)
    request_id= models.ForeignKey(StoreRequest, related_name= 'storerequest_stocktransfer', on_delete=models.CASCADE)
    transfer_status= models.BooleanField(default=True)
    transfer_desc= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_at

class TransferDrug(models.Model):
    REQUEST_STATUS = (
        ('REQ', 'requested'),
        ('TRA', 'transfer'),
        ('PUR', 'purchased'),
        ('CLS', 'closed'),
    )
    id= models.AutoField(primary_key=True)
    drug_id= models.ForeignKey(Drug, on_delete=models.CASCADE, related_name= 'drug_transfer_drug')
    from_stock_id= models.ForeignKey(StoreStock, on_delete=models.CASCADE,related_name='stocktransfer_stock_from')
    to_stock_id= models.ForeignKey(StoreStock, on_delete=models.CASCADE,related_name='stocktransfer_stock_to')
    transfer_id= models.ForeignKey(StockTransfer, on_delete=models.CASCADE, related_name= 'stock_transfer_transfer_drug')
    transfer_drug_quantity= models.IntegerField()
    transfer_drug_status= models.CharField(choices=REQUEST_STATUS, default='REQ', max_length=9)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)