# Generated by Django 2.1.2 on 2018-11-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotorwayEvent',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('motorway', models.IntegerField(choices=[(6, 6)])),
                ('direction', models.CharField(choices=[('n', 'n'), ('s', 's'), ('e', 'e'), ('w', 'w')], max_length=1)),
                ('junction', models.CharField(max_length=255)),
                ('metadata', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
                ('closest_cities', models.CharField(max_length=255)),
                ('time_timestamp', models.CharField(max_length=255)),
                ('time_day_worded', models.CharField(choices=[('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thu', 'Thu'), ('Fri', 'Fri')], max_length=3)),
                ('time_year', models.IntegerField(choices=[(2017, 2017), (2018, 2018)])),
                ('time_day_numerical', models.IntegerField()),
                ('time_hour', models.IntegerField()),
                ('time_minutes', models.IntegerField()),
                ('time_seconds', models.IntegerField()),
            ],
        ),
    ]
