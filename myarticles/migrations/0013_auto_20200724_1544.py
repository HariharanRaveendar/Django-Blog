# Generated by Django 3.0.8 on 2020-07-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myarticles', '0012_auto_20200724_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myarticle',
            name='Body1',
        ),
        migrations.AddField(
            model_name='myarticle',
            name='Body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
