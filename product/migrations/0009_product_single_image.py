# Generated by Django 4.2.5 on 2024-03-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='single_image',
            field=models.ImageField(blank=True, default='NO image is available', null=True, upload_to='product_image'),
        ),
    ]