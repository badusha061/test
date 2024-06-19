# Generated by Django 4.2.5 on 2023-10-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0028_alter_order_od_status_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='od_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Processing', 'Processing'), ('Return', 'Return'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='pending', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Processing', 'Processing'), ('Return', 'Return'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='pendings', max_length=150),
        ),
    ]
