# Generated by Django 2.0 on 2018-01-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180103_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateField(blank=True, help_text='(.etc 2018-01-06)', null=True, verbose_name='Date Published'),
        ),
    ]
