# Generated by Django 3.1.3 on 2021-08-14 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honameuro', '0007_auto_20210814_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='indiv',
        ),
    ]
