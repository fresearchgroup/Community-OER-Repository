# Generated by Django 2.0.5 on 2018-06-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_articles_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_id',
            field=models.IntegerField(default=0),
        ),
    ]
