# Generated by Django 4.1.8 on 2023-06-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='invoice_atm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='invoice_number',
            field=models.IntegerField(null=True),
        ),
    ]