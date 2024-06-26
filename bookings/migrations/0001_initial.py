# Generated by Django 3.2.25 on 2024-03-27 17:35

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
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(unique=True)),
                ('table_num_seats', models.IntegerField(choices=[(2, 4), (6, 2), (8, 1)], default=2)),
            ],
            options={
                'ordering': ['table_number'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('party_size', models.IntegerField(default=2)),
                ('booking_date', models.DateField()),
                ('booking_time', models.IntegerField(choices=[(12, '12:00'), (18, '18:00'), (20, '20:00')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('allergies', models.CharField(blank=True, max_length=200)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='Bookings.table')),
            ],
            options={
                'ordering': ['booking_date', 'booking_time'],
            },
        ),
    ]
