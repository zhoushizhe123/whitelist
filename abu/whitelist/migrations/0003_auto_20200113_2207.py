# Generated by Django 2.1 on 2020-01-13 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whitelist', '0002_ip_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='update',
            new_name='created',
        ),
    ]