# Generated by Django 4.2.7 on 2023-12-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tort',
            name='photo',
            field=models.FileField(upload_to='tort/', verbose_name='photo:'),
        ),
        migrations.AlterField(
            model_name='tort',
            name='qurami',
            field=models.TextField(verbose_name='qurami:'),
        ),
    ]
