# Generated by Django 4.2.3 on 2023-09-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_alter_order_address_alter_order_od_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='order',
            name='od_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered'), ('Return', 'Return'), ('Shipped', 'Shipped'), ('Processing', 'Processing')], default='pending', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered'), ('Return', 'Return'), ('Shipped', 'Shipped'), ('Processing', 'Processing')], default='pendings', max_length=150),
        ),
    ]