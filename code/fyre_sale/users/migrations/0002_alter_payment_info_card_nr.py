# Generated by Django 4.0.4 on 2022-05-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_info',
            name='card_nr',
            field=models.CharField(default=None, max_length=16),
        ),
    ]
