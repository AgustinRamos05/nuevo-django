# Generated by Django 4.2.6 on 2023-11-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('memoria', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
