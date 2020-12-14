# Generated by Django 2.2.5 on 2020-12-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20201125_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='baths',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='bedrooms',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='beds',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]