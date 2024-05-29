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
        return super().get_queryset().using("read_only_db2")


class AdmCantFeedData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "adm_cant_feed_data"


class ChilTr1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "chil_tr1_data"


class CrechData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "crech_data"


class GeneralPdbData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "general_pdb_data"


class HvacFeederData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "hvac_feeder_data"


class Lamin1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "lamin1_data"


class Lamin2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "lamin2_data"


class LightingDbData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "lighting_db_data"


class Mod1DailyKwh(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    pcc2_incm = models.BigIntegerField(
        db_column="pcc2_incm", blank=True, null=True
    )  # Field name made lowercase.
    hvac = models.BigIntegerField(
        db_column="hvac", blank=True, null=True
    )  # Field name made lowercase.
    util_feed = models.BigIntegerField(
        db_column="util_feed", blank=True, null=True
    )  # Field name made lowercase.
    ups_incm1 = models.BigIntegerField(
        db_column="ups_incm1", blank=True, null=True
    )  # Field name made lowercase.
    ups_incm2 = models.BigIntegerField(
        db_column="ups_incm2", blank=True, null=True
    )  # Field name made lowercase.
    ups_incm3 = models.BigIntegerField(
        db_column="ups_incm3", blank=True, null=True
    )  # Field name made lowercase.
    ups_incm4 = models.BigIntegerField(
        db_column="ups_incm4", blank=True, null=True
    )  # Field name made lowercase.
    ups_incm5 = models.BigIntegerField(
        db_column="ups_incm5", blank=True, null=True
    )  # Field name made lowercase.
    adm_cant_feed = models.BigIntegerField(
        db_column="adm_cant_feed", blank=True, null=True
    )  # Field name made lowercase.
    lighting_db = models.BigIntegerField(
        db_column="lighting_db", blank=True, null=True
    )  # Field name made lowercase.
    crech = models.BigIntegerField(
        db_column="crech", blank=True, null=True
    )  # Field name made lowercase.
    gen_pdb = models.BigIntegerField(
        db_column="gen_pdb", blank=True, null=True
    )  # Field name made lowercase.
    pcc1_incm = models.BigIntegerField(
        db_column="pcc1_incm", blank=True, null=True
    )  # Field name made lowercase.
    solar_feed = models.BigIntegerField(
        db_column="solar_feed", blank=True, null=True
    )  # Field name made lowercase.
    lamin1 = models.BigIntegerField(
        db_column="lamin1", blank=True, null=True
    )  # Field name made lowercase.
    lamin2 = models.BigIntegerField(
        db_column="lamin2", blank=True, null=True
    )  # Field name made lowercase.
    chill_tr1 = models.BigIntegerField(
        db_column="chill_tr1", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "mod1_daily_kwh"


class Pcc1IncmData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "pcc1_incm_data"


class Pcc2IncmData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "pcc2_incm_data"


class SolarFeederData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "solar_feeder_data"


class UpsIncm1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "ups_incm1_data"


class UpsIncm2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "ups_incm2_data"


class UpsIncm3Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "ups_incm3_data"


class UpsIncm4Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "ups_incm4_data"


class UpsIncm5Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "ups_incm5_data"


class UtilFeedData(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    avg_voltage = models.FloatField(
        db_column="avg_voltage", blank=True, null=True
    )  # Field name made lowercase.
    avg_current = models.BigIntegerField(
        db_column="avg_current", blank=True, null=True
    )  # Field name made lowercase.
    kwh = models.BigIntegerField(
        db_column="kwh", blank=True, null=True
    )  # Field name made lowercase.
    kw = models.IntegerField(
        db_column="kw", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "util_feed_data"
