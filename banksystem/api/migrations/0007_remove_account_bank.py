# Generated by Django 5.1 on 2024-09-01 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_account_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='bank',
        ),
    ]
