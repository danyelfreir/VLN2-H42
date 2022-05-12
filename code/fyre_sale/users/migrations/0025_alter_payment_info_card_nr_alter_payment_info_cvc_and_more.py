# Generated by Django 4.0.4 on 2022-05-12 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0024_alter_payment_info_card_nr_alter_payment_info_cvc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_info',
            name='card_nr',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='cvc',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='expires',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
