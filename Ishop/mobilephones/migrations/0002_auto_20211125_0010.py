# Generated by Django 2.2.19 on 2021-11-24 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobilephones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='manager',
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
        ),
        migrations.AddField(
            model_name='mobile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mobiles', to='mobilephones.Group'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
