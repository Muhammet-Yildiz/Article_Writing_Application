# Generated by Django 3.1.4 on 2021-01-27 14:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0011_auto_20210127_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='dislikes',
            field=models.ManyToManyField(related_name='answer_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(related_name='answer_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
