# Generated by Django 3.1.4 on 2021-02-01 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0016_delete_comment2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cevap yazarı '),
        ),
    ]
