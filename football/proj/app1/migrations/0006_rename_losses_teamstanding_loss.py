# Generated by Django 5.1.6 on 2025-03-04 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_teamstanding_delete_standing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamstanding',
            old_name='losses',
            new_name='loss',
        ),
    ]
