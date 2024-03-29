# Generated by Django 2.2 on 2019-06-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mis_task',
            fields=[
                ('task_id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=50)),
                ('patrol_circuit', models.CharField(max_length=50)),
                ('Inspector', models.CharField(max_length=30)),
                ('enabled_state', models.CharField(max_length=20)),
                ('Initial_pole_number', models.CharField(max_length=50)),
                ('termination_pole_number', models.CharField(max_length=50)),
                ('sender', models.CharField(max_length=20)),
                ('departure_time', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mis_task',
            },
        ),
    ]
