# Generated by Django 2.1.5 on 2023-09-21 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='descritption',
            new_name='description',
        ),
    ]
