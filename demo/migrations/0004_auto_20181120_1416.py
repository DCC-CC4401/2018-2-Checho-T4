# Generated by Django 2.1.3 on 2018-11-20 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20181120_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='estudiante',
            new_name='usuario',
        ),
    ]