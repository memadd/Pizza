# Generated by Django 3.0.3 on 2020-02-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200214_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lprice',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sprice',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
