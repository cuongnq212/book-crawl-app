# Generated by Django 2.1 on 2019-12-01 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20191128_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-price_int',)},
        ),
    ]
