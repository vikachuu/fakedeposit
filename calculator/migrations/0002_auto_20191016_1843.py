# Generated by Django 2.2.1 on 2019-10-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculatorpage',
            old_name='intro',
            new_name='text',
        ),
    ]
