# Generated by Django 4.0.4 on 2022-05-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.TextField(default=None, max_length=9999),
        ),
    ]
