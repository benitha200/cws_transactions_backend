# Generated by Django 5.0.1 on 2024-01-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='paper_grn_no',
            field=models.TextField(max_length=20),
        ),
    ]
