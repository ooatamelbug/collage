# Generated by Django 4.1.8 on 2023-04-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_first_name', models.CharField(max_length=25)),
                ('supplier_middle_name', models.CharField(max_length=25)),
                ('supplier_last_name', models.CharField(max_length=25)),
                ('supplier_address', models.CharField(max_length=25)),
                ('supplier_aphone1', models.CharField(max_length=25)),
                ('supplier_aphone2', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
