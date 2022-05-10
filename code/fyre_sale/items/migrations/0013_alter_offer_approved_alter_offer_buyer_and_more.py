# Generated by Django 4.0.4 on 2022-05-10 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0012_alter_itemforsale_cur_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='approved',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='offer',
            name='buyer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='items.itemforsale'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_of_offer',
            field=models.DateTimeField(blank=True),
        ),
    ]
