from django.db import models
from store.models import Store
from drug.models import Drug
from users.models import User
# Create your models here.

class StoreRequest(models.Model):
    id= models.AutoField(primary_key=True)
    request_desc= models.TextField()
    request_status= models.BooleanField(default=False)
    user_id= models.ForeignKey(User,null=True, related_name= 'user_request', on_delete=models.CASCADE)
    store_id= models.ForeignKey(Store, related_name= 'store_store_request', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.request_desc

class RequestDrug(models.Model):
    REQUEST_STATUS = (
        ('REQ', 'requested'),
        ('PUR', 'purchased'),
        ('CLS', 'closed'),
    )
    id= models.AutoField(primary_key=True)
    request_id= models.ForeignKey(StoreRequest,null=True, related_name= 'store_requested', on_delete=models.CASCADE)
    drug_id= models.ForeignKey(Drug, related_name= 'drug_store_request', on_delete=models.CASCADE)
    request_drug_quantity= models.IntegerField()
    request_status= models.CharField(choices=REQUEST_STATUS,default='REQ', max_length=9)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.request_status
