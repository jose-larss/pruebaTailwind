# Generated by Django 4.1.5 on 2023-01-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_banderas_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banderas',
            name='imagen',
            field=models.CharField(max_length=25),
        ),
    ]