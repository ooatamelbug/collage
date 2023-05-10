from django.db import models
from users.models import User
from store.models import Store
from stock.models import StoreStock
from drug.models import Drug
# Create your models here.


class Dispensing(models.Model):
    id= models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field="id", related_name='user_dispensing', on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, to_field="id", related_name='store_dispensing', on_delete=models.CASCADE)
    total_price= models.FloatField(default=0.0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.total_price)

class SoldDrug(models.Model):
    id= models.AutoField(primary_key=True)
    sold_quantity= models.IntegerField()
    sell_price= models.FloatField(default=0.0)
    dispensing_id= models.ForeignKey(Dispensing, to_field="id", related_name='dispensing_drug', on_delete=models.CASCADE)
    store_stock_id= models.ForeignKey(StoreStock, related_name='store_stock_drug', on_delete=models.CASCADE)
    drug_id= models.ForeignKey(Drug, related_name='drug_sold_drug', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.dispensing_id)