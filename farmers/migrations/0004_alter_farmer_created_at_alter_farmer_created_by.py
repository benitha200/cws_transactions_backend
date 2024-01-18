# Generated by Django 5.0.1 on 2024-01-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_farmer_cws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='created_by',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
