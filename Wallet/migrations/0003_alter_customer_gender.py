# Generated by Django 4.1.1 on 2022-09-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0002_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]