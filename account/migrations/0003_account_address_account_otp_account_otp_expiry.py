# Generated by Django 5.1.4 on 2024-12-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
