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
        return super().get_queryset().using("read_only_db3")


class CellLtPanel1Data(models.Model):
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
        db_table = "cell_lt_panel1_data"


class CellLtPanel2Data(models.Model):
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

    class Meta:
        managed = False
        db_table = "cell_lt_panel2_data"


class CellToolPdb1Data(models.Model):
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
        db_table = "cell_tool_pdb1_data"


class CellToolPdb2Data(models.Model):
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
        db_table = "cell_tool_pdb2_data"


class Chiller2Data(models.Model):
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
        db_table = "chiller2_data"


class Pcc1DailyKwh(models.Model):
    date_time = models.DateTimeField(
        primary_key=True, db_column="date_time"
    )  # Field name made lowercase.
    chiller2 = models.BigIntegerField(
        db_column="chiller2", blank=True, null=True
    )  # Field name made lowercase.
    cell_lt_pnl1 = models.BigIntegerField(
        db_column="cell_lt_pnl1", blank=True, null=True
    )  # Field name made lowercase.
    cell_tool_pdb1 = models.BigIntegerField(
        db_column="cell_tool_pdb1", blank=True, null=True
    )  # Field name made lowercase.
    pcc1_incm = models.BigIntegerField(
        db_column="pcc1_incm", blank=True, null=True
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
    pcc2_incm = models.BigIntegerField(
        db_column="pcc2_incm", blank=True, null=True
    )  # Field name made lowercase.
    cell_lt_pnl2 = models.BigIntegerField(
        db_column="cell_lt_pnl2", blank=True, null=True
    )  # Field name made lowercase.
    cell_tool_pdb2 = models.BigIntegerField(
        db_column="cell_tool_pdb2", blank=True, null=True
    )  # Field name made lowercase.
    ups2_og1 = models.BigIntegerField(
        db_column="ups2_og1", blank=True, null=True
    )  # Field name made lowercase.
    ups2_og2 = models.BigIntegerField(
        db_column="ups2_og2", blank=True, null=True
    )  # Field name made lowercase.
    ups2_og3 = models.BigIntegerField(
        db_column="ups2_og3", blank=True, null=True
    )  # Field name made lowercase.
    ups2_og4 = models.BigIntegerField(
        db_column="ups2_og4", blank=True, null=True
    )  # Field name made lowercase.
    ups2_og5 = models.BigIntegerField(
        db_column="ups2_og5", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = False
        db_table = "pcc1_daily_kwh"


class Pcc1IncomerData(models.Model):
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
        db_table = "pcc1_incomer_data"


class Pcc2IncomerData(models.Model):
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
        db_table = "pcc2_incomer_data"


class Ups1Og1Data(models.Model):
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
        db_table = "ups1_og1_data"


class Ups1Og2Data(models.Model):
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
        db_table = "ups1_og2_data"


class Ups1Og3Data(models.Model):
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
        db_table = "ups1_og3_data"


class Ups1Og4Data(models.Model):
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
        db_table = "ups1_og4_data"


class Ups1Og5Data(models.Model):
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
        db_table = "ups1_og5_data"


class Ups2Og1Data(models.Model):
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
        db_table = "ups2_og1_data"


class Ups2Og2Data(models.Model):
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
        db_table = "ups2_og2_data"


class Ups2Og3Data(models.Model):
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
        db_table = "ups2_og3_data"


class Ups2Og4Data(models.Model):
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
        db_table = "ups2_og4_data"


class Ups2Og5Data(models.Model):
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
        db_table = "ups2_og5_data"
