from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.StockTransfer)
admin.site.register(models.TransferDrug)
