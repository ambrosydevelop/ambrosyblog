# Generated by Django 3.2.4 on 2022-06-06 19:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0012_auto_20220605_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='view_author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2022, 6, 7, 0, 3, 38, 1906)),
        ),
    ]
