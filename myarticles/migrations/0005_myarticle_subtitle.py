# Generated by Django 3.0.8 on 2020-07-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myarticles', '0004_auto_20200724_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='myarticle',
            name='SubTitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
