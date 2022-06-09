# Generated by Django 3.2.4 on 2022-06-06 19:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0014_alter_article_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='view',
        ),
        migrations.RemoveField(
            model_name='article',
            name='view_author',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2022, 6, 7, 0, 7, 7, 518217)),
        ),
        migrations.CreateModel(
            name='ArticleView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_view_field', to='article.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_view_field', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]