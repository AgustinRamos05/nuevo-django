# Generated by Django 4.2.6 on 2023-12-19 04:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iphone',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]