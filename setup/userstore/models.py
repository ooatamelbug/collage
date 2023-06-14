from django.db import models
from users.models import User
from store.models import Store
# Create your models here.


class UserStore(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User,  on_delete=models.CASCADE, related_name='user_store')
    store_id = models.ForeignKey(
        Store,  on_delete=models.CASCADE ,related_name='store_user')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.store_id) + " work in " + str(self.user_id)
