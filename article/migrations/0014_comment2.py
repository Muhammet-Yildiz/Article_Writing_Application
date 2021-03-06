# Generated by Django 3.1.4 on 2021-02-01 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0013_auto_20210127_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content2', models.CharField(max_length=100, verbose_name='Yorum ')),
                ('comment_date2', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment_related', to='article.article', verbose_name='Baglı makale')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='yorum yazarı ')),
                ('dislikes2', models.ManyToManyField(related_name='Related_comment_dislike2', to=settings.AUTH_USER_MODEL)),
                ('likes2', models.ManyToManyField(related_name='Related_comment_like2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
