# Generated by Django 4.0.4 on 2022-05-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_get_back_money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getbackmoney',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
