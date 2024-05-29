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
        return super().get_queryset().using("read_only_db5")


class Cell1DailyKwh(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
    )  # Field name made lowercase.
    ups1_incm1 = models.BigIntegerField(
        db_column="ups1_incm1", blank=True, null=True
    )  # Field name made lowercase.
    ups1_incm2 = models.BigIntegerField(
        db_column="ups1_incm2", blank=True, null=True
    )  # Field name made lowercase.
    ups1_incm3 = models.BigIntegerField(
        db_column="ups1_incm3", blank=True, null=True
    )  # Field name made lowercase.
    ups1_incm4 = models.BigIntegerField(
        db_column="ups1_incm4", blank=True, null=True
    )  # Field name made lowercase.
    ups1_incm5 = models.BigIntegerField(
        db_column="ups1_incm5", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og1 = models.BigIntegerField(
        db_column="ups1_og1", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og2 = models.BigIntegerField(
        db_column="ups1_og2", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og3 = models.BigIntegerField(
        db_column="ups1_og3", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og4 = models.BigIntegerField(
        db_column="ups1_og4", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og5 = models.BigIntegerField(
        db_column="ups1_og5", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og_acb1 = models.BigIntegerField(
        db_column="ups1_og_acb1", blank=True, null=True
    )  # Field name made lowercase.
    ups1_og_acb2 = models.BigIntegerField(
        db_column="ups1_og_acb2", blank=True, null=True
    )  # Field name made lowercase.
    ups1_lt_pnl1 = models.BigIntegerField(
        db_column="ups1_lt_pnl1", blank=True, null=True
    )  # Field name made lowercase.
    ups1_lt_pnl2 = models.BigIntegerField(
        db_column="ups1_lt_pnl2", blank=True, null=True
    )  # Field name made lowercase.
    cell_lt_pnl1 = models.BigIntegerField(
        db_column="cell_lt_pnl1", blank=True, null=True
    )  # Field name made lowercase.
    cell_lt_pnl2 = models.BigIntegerField(
        db_column="cell_lt_pnl2", blank=True, null=True
    )  # Field name made lowercase.
    hwt1 = models.BigIntegerField(
        db_column="hwt1", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "cell1_daily_kwh"


class CellLtPanel1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "cell_lt_panel1_data"


class CellLtPanel2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "cell_lt_panel2_data"


class Hwt1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "hwt1_data"


class Ups1Incomer1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_incomer1_data"


class Ups1Incomer2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_incomer2_data"


class Ups1Incomer3Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_incomer3_data"


class Ups1Incomer4Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_incomer4_data"


class Ups1Incomer5Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_incomer5_data"


class Ups1LtPanel1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_lt_panel1_data"


class Ups1LtPanel2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_lt_panel2_data"


class Ups1Og1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og1_data"


class Ups1Og2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og2_data"


class Ups1Og3Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og3_data"


class Ups1Og4Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og4_data"


class Ups1Og5Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og5_data"


class Ups1OgAcb1Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og_acb1_data"


class Ups1OgAcb2Data(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time", blank=True
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
        db_table = "ups1_og_acb2_data"
