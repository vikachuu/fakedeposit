# Generated by Django 2.2.1 on 2019-11-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit_tax', '0002_auto_20191019_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposittaxpage',
            name='page_description',
            field=models.CharField(default='string', max_length=200),
        ),
    ]