# Generated by Django 3.1.3 on 2021-08-14 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('honameuro', '0009_indivinfo_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indivinfo',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='honameuro.topic'),
        ),
        migrations.CreateModel(
            name='IndivTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indiv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='honameuro.indivinfo')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='honameuro.topic')),
            ],
        ),
    ]
