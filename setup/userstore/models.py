from django.db import models
from users.models import User
from store.models import Store
# Create your models here.

class UserStore(models.Model):
    id= models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, related_name= 'user_userstore', on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, related_name= 'store_userstore', on_delete=models.CASCADE)
    status= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.store_id + " work in " +self.user_id