# Generated by Django 4.1.8 on 2023-05-04 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0001_initial'),
        ('dispensing', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solddrug',
            name='drug_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drug_sold_drug', to='drug.drug'),
        ),
    ]
