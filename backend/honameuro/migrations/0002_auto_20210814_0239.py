# Generated by Django 3.1.3 on 2021-08-13 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honameuro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='villageinfo',
            old_name='vi_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='villageinfo',
            old_name='vi_create_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='villageinfo',
            old_name='vi_max',
            new_name='max',
        ),
        migrations.RenameField(
            model_name='villageinfo',
            old_name='vi_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='villageinfo',
            old_name='vi_selected',
            new_name='selected',
        ),
        migrations.RenameField(
            model_name='villageinfo',
            old_name='vi_title',
            new_name='title',
        ),
    ]
