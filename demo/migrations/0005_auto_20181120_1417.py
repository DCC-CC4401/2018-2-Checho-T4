# Generated by Django 2.1.3 on 2018-11-20 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20181120_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='usuario',
            new_name='persona',
        ),
    ]