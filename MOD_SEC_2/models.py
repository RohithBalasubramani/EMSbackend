# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class YourCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('read_only_db4')

class Aircomp1Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'AIRCOMP1_DATA'


class Aircomp2Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'AIRCOMP2_DATA'


class Aircomp3Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'AIRCOMP3_DATA'


class Aircomp4Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'AIRCOMP4_DATA'


class ChlTr2Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'CHL_TR2_DATA'


class GenPdbData(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'GEN_PDB_DATA'


class Lamin3Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'LAMIN3_DATA'


class Lamin4Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'LAMIN4_DATA'


class LightDbData(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'LIGHT_DB_DATA'


class Mod2DailyKwh(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    lamin4 = models.BigIntegerField(db_column='LAMIN4', blank=True, null=True)  # Field name made lowercase.
    lamin3 = models.BigIntegerField(db_column='LAMIN3', blank=True, null=True)  # Field name made lowercase.
    chill_tr2 = models.BigIntegerField(db_column='CHILL_TR2', blank=True, null=True)  # Field name made lowercase.
    aircomp4 = models.BigIntegerField(db_column='AIRCOMP4', blank=True, null=True)  # Field name made lowercase.
    aircomp3 = models.BigIntegerField(db_column='AIRCOMP3', blank=True, null=True)  # Field name made lowercase.
    aircomp2 = models.BigIntegerField(db_column='AIRCOMP2', blank=True, null=True)  # Field name made lowercase.
    aircomp1 = models.BigIntegerField(db_column='AIRCOMP1', blank=True, null=True)  # Field name made lowercase.
    gen_pdb = models.BigIntegerField(db_column='GEN_PDB', blank=True, null=True)  # Field name made lowercase.
    lighting_db = models.BigIntegerField(db_column='LIGHTING_DB', blank=True, null=True)  # Field name made lowercase.
    ups_og1 = models.BigIntegerField(db_column='UPS_OG1', blank=True, null=True)  # Field name made lowercase.
    ups_og2 = models.BigIntegerField(db_column='UPS_OG2', blank=True, null=True)  # Field name made lowercase.
    ups_og3 = models.BigIntegerField(db_column='UPS_OG3', blank=True, null=True)  # Field name made lowercase.
    ups_og4 = models.BigIntegerField(db_column='UPS_OG4', blank=True, null=True)  # Field name made lowercase.
    ups_og5 = models.BigIntegerField(db_column='UPS_OG5', blank=True, null=True)  # Field name made lowercase.
    ups_lt_og1 = models.BigIntegerField(db_column='UPS_LT_OG1', blank=True, null=True)  # Field name made lowercase.
    ups_lt_og2 = models.BigIntegerField(db_column='UPS_LT_OG2', blank=True, null=True)  # Field name made lowercase.
    ups_lt_og3 = models.BigIntegerField(db_column='UPS_LT_OG3', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'MOD2_DAILY_KWH'


class UpsLtOg1Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_LT_OG1_DATA'


class UpsLtOg2Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_LT_OG2_DATA'


class UpsLtOg3Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_LT_OG3_DATA'


class UpsOg1Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_OG1_DATA'


class UpsOg2Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_OG2_DATA'


class UpsOg3Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_OG3_DATA'


class UpsOg4Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_OG4_DATA'


class UpsOg5Data(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column='DATE_TIME')  # Field name made lowercase.
    avg_voltage = models.FloatField(db_column='AVG_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.BigIntegerField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    kwh = models.BigIntegerField(db_column='KWH', blank=True, null=True)  # Field name made lowercase.
    kw = models.IntegerField(db_column='KW', blank=True, null=True)  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = 'UPS_OG5_DATA'
