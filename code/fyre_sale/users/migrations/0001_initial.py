# Generated by Django 4.0.4 on 2022-05-12 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address_info',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('street_name', models.CharField(default=None, max_length=255)),
                ('zip', models.CharField(default=None, max_length=15)),
                ('city', models.CharField(default=None, max_length=255)),
                ('country', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_info',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('card_nr', models.CharField(default=None, max_length=20)),
                ('expires', models.CharField(default=None, max_length=10)),
                ('cvc', models.CharField(default=None, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profileimg', models.ImageField(blank=True, default='profile-icon.png', null=True, upload_to='')),
                ('bio', models.TextField(blank=True, default=None, max_length=9999, null=True)),
                ('birthday', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_rating',
            fields=[
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_rating', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.offer')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
