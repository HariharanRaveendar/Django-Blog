# Generated by Django 3.0.8 on 2020-07-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=250)),
                ('MsgSubject', models.TextField(null=True)),
                ('MsgBody', models.TextField()),
                ('DateSent', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
