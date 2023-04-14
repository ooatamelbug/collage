# Generated by Django 4.1.8 on 2023-04-14 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drug', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_desc', models.TextField()),
                ('request_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_store_request', to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='RequestDrug',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_drug_quantity', models.IntegerField()),
                ('request_status', models.CharField(choices=[('REQ', 'requested'), ('PUR', 'purchased'), ('CLS', 'closed')], default='REQ', max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_store_request', to='drug.drug')),
            ],
        ),
    ]