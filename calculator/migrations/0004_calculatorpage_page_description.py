# Generated by Django 2.2.1 on 2019-11-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20191018_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculatorpage',
            name='page_description',
            field=models.CharField(default='string', max_length=200),
        ),
    ]
