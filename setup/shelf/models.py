from django.db import models
from store.models import Store
from stock.models import StoreStock
# Create your models here.

class Shelf(models.Model):
    id=models.AutoField(primary_key=True)
    shelf_name= models.CharField(max_length=25)
    shelf_location= models.CharField(max_length=25)
    store_id= models.ForeignKey(Store, related_name= 'store', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.shelf_name
    

class ShelfDrug(models.Model):
    id=models.AutoField(primary_key=True)
    shelf_id = models.ForeignKey(Shelf, related_name= 'shelf', on_delete=models.CASCADE)
    store_stock_id = models.ForeignKey(StoreStock, related_name= 'storestock', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.store_stock_id