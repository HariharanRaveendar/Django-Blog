# Generated by Django 3.0.8 on 2020-07-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myarticles', '0016_auto_20200729_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myarticle',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
    ]
