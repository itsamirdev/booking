# Generated by Django 4.2.4 on 2023-08-25 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('postal_code', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.address')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_count', models.IntegerField()),
                ('status', models.CharField(choices=[('READY', 'Ready'), ('UNDER_REPAIR', 'Under Repair'), ('RESERVED', 'Reserved'), ('Inaccessible', 'Inaccessible')], default='READY', max_length=12)),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('APPROVED', 'Approved'), ('PENDING', 'Pending'), ('FAILED', 'Failed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('national_code', models.CharField(max_length=16, unique=True)),
                ('reservation_date', models.DateField()),
                ('reservation_days', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.hotel')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='rooms',
            field=models.ManyToManyField(to='hotel.room'),
        ),
    ]
