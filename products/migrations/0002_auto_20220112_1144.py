# Generated by Django 3.1.6 on 2022-01-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='stripe_price_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
