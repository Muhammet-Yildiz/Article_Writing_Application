# Generated by Django 3.1.4 on 2021-01-26 18:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0007_comment_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(related_name='Related_comment_dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
