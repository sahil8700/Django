# Generated by Django 3.0.4 on 2020-03-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200317_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
