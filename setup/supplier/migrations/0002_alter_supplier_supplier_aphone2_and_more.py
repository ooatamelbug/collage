# Generated by Django 4.1.8 on 2023-06-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_aphone2',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_middle_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]