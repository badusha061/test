# Generated by Django 4.2.3 on 2023-09-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_category_image_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='No image available', upload_to='photos/name'),
        ),
    ]
