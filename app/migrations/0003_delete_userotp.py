# Generated by Django 4.0.2 on 2022-02-25 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userotp_verification_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserOtp',
        ),
    ]
