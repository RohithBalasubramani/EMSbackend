# Generated by Django 5.0.4 on 2024-04-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amf1DailyKwh',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('apfc2_kwh', models.BigIntegerField(blank=True, db_column='apfc2_kwh', null=True)),
                ('tf2_kwh', models.BigIntegerField(blank=True, db_column='tf2_kwh', null=True)),
                ('dg2_kwh', models.BigIntegerField(blank=True, db_column='dg2_kwh', null=True)),
                ('og2_kwh', models.BigIntegerField(blank=True, db_column='og2_kwh', null=True)),
                ('og1_kwh', models.BigIntegerField(blank=True, db_column='og1_kwh', null=True)),
                ('dg1_kwh', models.BigIntegerField(blank=True, db_column='dg1_kwh', null=True)),
                ('tf1_kwh', models.BigIntegerField(blank=True, db_column='tf1_kwh', null=True)),
                ('apfc1_kwh', models.BigIntegerField(blank=True, db_column='apfc1_kwh', null=True)),
            ],
            options={
                'db_table': 'amf1_daily_kwh',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Amf2DailyKwh',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('apfc4_kwh', models.BigIntegerField(blank=True, db_column='apfc4_kwh', null=True)),
                ('tf4_kwh', models.BigIntegerField(blank=True, db_column='tf4_kwh', null=True)),
                ('dg4_kwh', models.BigIntegerField(blank=True, db_column='dg4_kwh', null=True)),
                ('og4_kwh', models.BigIntegerField(blank=True, db_column='og4_kwh', null=True)),
                ('og3_kwh', models.BigIntegerField(blank=True, db_column='og3_kwh', null=True)),
                ('dg3_kwh', models.BigIntegerField(blank=True, db_column='dg3_kwh', null=True)),
                ('tf3_kwh', models.BigIntegerField(blank=True, db_column='tf3_kwh', null=True)),
                ('apfc3_kwh', models.BigIntegerField(blank=True, db_column='apfc3_kwh', null=True)),
            ],
            options={
                'db_table': 'amf2_daily_kwh',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Amf3Daily',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('apfc5_daily', models.BigIntegerField(blank=True, db_column='apfc5_daily', null=True)),
                ('tf5_daily', models.BigIntegerField(blank=True, db_column='tf5_daily', null=True)),
                ('dg5_daily', models.BigIntegerField(blank=True, db_column='dg5_daily', null=True)),
                ('dg6_daily', models.BigIntegerField(blank=True, db_column='dg6_daily', null=True)),
                ('og5_daily', models.BigIntegerField(blank=True, db_column='og5_daily', null=True)),
                ('og6_daily', models.BigIntegerField(blank=True, db_column='og6_daily', null=True)),
                ('sol_daily', models.BigIntegerField(blank=True, db_column='sol_daily', null=True)),
            ],
            options={
                'db_table': 'amf3_daily',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Apfc1Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.IntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.IntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.IntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.IntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
                ('pf', models.FloatField(blank=True, db_column='pf', null=True)),
            ],
            options={
                'db_table': 'apfc1_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Apfc2Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.IntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.IntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.IntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.IntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
                ('pf', models.FloatField(blank=True, db_column='pf', null=True)),
            ],
            options={
                'db_table': 'apfc2_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Apfc3Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.IntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.IntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.IntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.IntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
                ('pf', models.FloatField(blank=True, db_column='pf', null=True)),
            ],
            options={
                'db_table': 'apfc3_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Apfc4Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.IntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.IntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.IntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.IntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
                ('pf', models.FloatField(blank=True, db_column='pf', null=True)),
            ],
            options={
                'db_table': 'apfc4_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Apfc5Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.IntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.IntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.IntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.IntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
                ('pf', models.FloatField(blank=True, db_column='pf', null=True)),
            ],
            options={
                'db_table': 'apfc5_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dg1Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'dg1_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dg2Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'dg2_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dg3Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(db_column='total_units')),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'dg3_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dg4Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'dg4_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dg5Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'dg5_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dg6Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'dg6_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Og1Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'og1_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Og2Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'og2_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Og3Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'og3_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Og4Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'og4_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Og5Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'og5_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Og6Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'og6_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SolFeedData',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'sol_feed_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tf1Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'tf1_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tf2Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'tf2_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tf3Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'tf3_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tf4Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'tf4_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tf5Data',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('total_units', models.BigIntegerField(blank=True, db_column='total_units', null=True)),
                ('ll_vltg', models.FloatField(blank=True, db_column='ll_vltg', null=True)),
                ('avg_curr', models.BigIntegerField(blank=True, db_column='avg_curr', null=True)),
                ('r_curr', models.BigIntegerField(blank=True, db_column='r_curr', null=True)),
                ('y_curr', models.BigIntegerField(blank=True, db_column='y_curr', null=True)),
                ('b_curr', models.BigIntegerField(blank=True, db_column='b_curr', null=True)),
                ('act_pwr', models.IntegerField(blank=True, db_column='act_pwr', null=True)),
            ],
            options={
                'db_table': 'tf5_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmT0',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, null=True)),
                ('final_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wm_t0',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmT1',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, null=True)),
                ('final_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wm_t1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmT2',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, null=True)),
                ('final_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wm_t2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm1',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, null=True)),
                ('final_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wm_wm1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm2',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm3',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm3',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm4',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm4',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm5',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm5',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm6',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm6',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm7',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm7',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm8',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm8',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WmWm9',
            fields=[
                ('date_time', models.DateTimeField(db_column='date_time', primary_key=True, serialize=False)),
                ('initial_value', models.IntegerField(blank=True, db_column='initial_value', null=True)),
                ('final_value', models.IntegerField(blank=True, db_column='final_value', null=True)),
            ],
            options={
                'db_table': 'wm_wm9',
                'managed': True,
            },
        ),
    ]
