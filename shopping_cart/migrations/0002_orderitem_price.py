# Generated by Django 3.0.3 on 2020-04-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
