# Generated by Django 4.2.3 on 2023-09-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men', models.CharField(blank=True, default=True, max_length=50, null=True)),
                ('women', models.CharField(blank=True, default=True, max_length=50, null=True)),
                ('kids', models.CharField(blank=True, default=True, max_length=50, null=True)),
            ],
        ),
    ]
