# Generated by Django 3.1 on 2020-09-17 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gas', '0007_auto_20200917_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='connection_number',
            field=models.CharField(blank=True, default='9488179160', editable=False, max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reffeling_size', models.CharField(choices=[('14.2', '14.2 KG'), ('5', '5 KG'), ('3', '3 KG')], max_length=10)),
                ('booking_number', models.CharField(blank=True, default='1950834815', editable=False, max_length=10, unique=True)),
                ('status', models.CharField(choices=[('1', 'Confirmed'), ('2', 'On The Way'), ('3', 'Delivered')], max_length=10)),
                ('date', models.DateField()),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gas.connection')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gas.staff')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
