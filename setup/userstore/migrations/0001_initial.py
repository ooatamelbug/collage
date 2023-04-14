# Generated by Django 4.1.8 on 2023-04-14 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStore',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_userstore', to='store.store')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_userstore', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
