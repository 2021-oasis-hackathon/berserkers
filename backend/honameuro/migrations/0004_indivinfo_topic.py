# Generated by Django 3.1.3 on 2021-08-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honameuro', '0003_auto_20210814_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='indivinfo',
            name='topic',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
