# Generated by Django 4.1.1 on 2022-09-12 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0007_loan_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=20)),
                ('balance', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_wallet', to='Wallet.wallet')),
            ],
        ),
    ]
