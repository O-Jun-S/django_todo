# Generated by Django 3.1.7 on 2021-03-03 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210303_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='destination_date',
            new_name='limit_date',
        ),
    ]