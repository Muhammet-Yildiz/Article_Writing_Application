# Generated by Django 3.1.4 on 2021-01-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_comment_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='unliked',
            field=models.BooleanField(default=False),
        ),
    ]