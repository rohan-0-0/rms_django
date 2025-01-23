# Generated by Django 5.1.5 on 2025-01-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0002_rename_table_id_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='description',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Completed')], default='P', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=1),
        ),
    ]
