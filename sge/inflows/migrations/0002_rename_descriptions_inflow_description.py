# Generated by Django 5.1.7 on 2025-04-14 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inflow',
            old_name='descriptions',
            new_name='description',
        ),
    ]
