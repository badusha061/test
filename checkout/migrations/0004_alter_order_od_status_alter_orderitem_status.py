# Generated by Django 4.2.3 on 2023-09-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_od_status_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='od_status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Return', 'Return'), ('Pending', 'Pending'), ('Shipped', 'Shipped')], default='pending', max_length=150),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Return', 'Return'), ('Pending', 'Pending'), ('Shipped', 'Shipped')], default='pendings', max_length=150),
        ),
    ]
