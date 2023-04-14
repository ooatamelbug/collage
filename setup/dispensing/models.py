from django.db import models
from users.models import User
from store.models import Store
from stock.models import StoreStock
# Create your models here.


class Dispensing(models.Model):
    id= models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, related_name='store', on_delete=models.CASCADE)
    total_price= models.FloatField(default=0.0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.total_price

class SoldDrug(models.Model):
    id= models.AutoField(primary_key=True)
    sold_quantity= models.IntegerField()
    sell_price= models.FloatField(default=0.0)
    dispensing_id= models.ForeignKey(Dispensing, related_name='dispensing', on_delete=models.CASCADE)
    store_stock_id= models.ForeignKey(StoreStock, related_name='store_stock', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.dispensing_id