# Generated by Django 3.1.4 on 2021-01-27 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20210127_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='dislikes',
            new_name='dislikess',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='likes',
            new_name='likess',
        ),
    ]