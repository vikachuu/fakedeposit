# Generated by Django 2.2.1 on 2019-11-09 18:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('deposit_bank_rates', '0002_auto_20191019_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('bank_name', models.CharField(default='string', max_length=100)),
                ('deposit_name', models.CharField(default='string', max_length=100)),
                ('income', models.BooleanField(default=False)),
                ('dolar', models.FloatField(default=0.0)),
                ('euro', models.FloatField(default=0.0)),
                ('hryvna', models.FloatField(default=0.0)),
                ('capitalization', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('bank_image', models.ImageField(default=None, upload_to='')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('full_body', wagtail.core.fields.RichTextField(blank=True)),
                ('page_description', models.CharField(default='string', max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
