# Generated by Django 3.1.3 on 2021-08-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honameuro', '0002_auto_20210814_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndivInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('max', models.PositiveSmallIntegerField()),
                ('selected', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='villageinfo',
            name='create_date',
        ),
    ]
