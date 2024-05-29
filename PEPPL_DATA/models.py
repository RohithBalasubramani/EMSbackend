from django.db import models


class YourCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using("read_only_db1")


class Amf1DailyKwh(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column="date_time")
    apfc2_kwh = models.BigIntegerField(db_column="apfc2_kwh", blank=True, null=True)
    tf2_kwh = models.BigIntegerField(db_column="tf2_kwh", blank=True, null=True)
    dg2_kwh = models.BigIntegerField(db_column="dg2_kwh", blank=True, null=True)
    og2_kwh = models.BigIntegerField(db_column="og2_kwh", blank=True, null=True)
    og1_kwh = models.BigIntegerField(db_column="og1_kwh", blank=True, null=True)
    dg1_kwh = models.BigIntegerField(db_column="dg1_kwh", blank=True, null=True)
    tf1_kwh = models.BigIntegerField(db_column="tf1_kwh", blank=True, null=True)
    apfc1_kwh = models.BigIntegerField(db_column="apfc1_kwh", blank=True, null=True)

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "amf1_daily_kwh"

    # def save(self, *args, **kwargs):
    #     # Explicitly specify the database where the instance should be saved
    #     kwargs["using"] = "postgres_db"
    #     super().save(*args, **kwargs)


class Amf2DailyKwh(models.Model):
    date_time = models.DateTimeField(primary_key=True, db_column="date_time")
    apfc4_kwh = models.BigIntegerField(db_column="apfc4_kwh", blank=True, null=True)
    tf4_kwh = models.BigIntegerField(db_column="tf4_kwh", blank=True, null=True)
    dg4_kwh = models.BigIntegerField(db_column="dg4_kwh", blank=True, null=True)
    og4_kwh = models.BigIntegerField(db_column="og4_kwh", blank=True, null=True)
    og3_kwh = models.BigIntegerField(db_column="og3_kwh", blank=True, null=True)
    dg3_kwh = models.BigIntegerField(db_column="dg3_kwh", blank=True, null=True)
    tf3_kwh = models.BigIntegerField(db_column="tf3_kwh", blank=True, null=True)
    apfc3_kwh = models.BigIntegerField(db_column="apfc3_kwh", blank=True, null=True)

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "amf2_daily_kwh"


class Amf3Daily(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    apfc5_daily = models.BigIntegerField(
        db_column="apfc5_daily", blank=True, null=True
    )  # Field name made lowercase.
    tf5_daily = models.BigIntegerField(
        db_column="tf5_daily", blank=True, null=True
    )  # Field name made lowercase.
    dg5_daily = models.BigIntegerField(
        db_column="dg5_daily", blank=True, null=True
    )  # Field name made lowercase.
    dg6_daily = models.BigIntegerField(
        db_column="dg6_daily", blank=True, null=True
    )  # Field name made lowercase.
    og5_daily = models.BigIntegerField(
        db_column="og5_daily", blank=True, null=True
    )  # Field name made lowercase.
    og6_daily = models.BigIntegerField(
        db_column="og6_daily", blank=True, null=True
    )  # Field name made lowercase.
    sol_daily = models.BigIntegerField(
        db_column="sol_daily", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "amf3_daily"


class Apfc1Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.IntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.IntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.IntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.IntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.
    pf = models.FloatField(
        db_column="pf", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "apfc1_data"


class Apfc2Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.IntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.IntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.IntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.IntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.
    pf = models.FloatField(
        db_column="pf", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "apfc2_data"


class Apfc3Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.IntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.IntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.IntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.IntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.
    pf = models.FloatField(
        db_column="pf", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "apfc3_data"


class Apfc4Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time", primary_key=True
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.IntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.IntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.IntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.IntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.
    pf = models.FloatField(
        db_column="pf", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "apfc4_data"


class Apfc5Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.IntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.IntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.IntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.IntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.
    pf = models.FloatField(
        db_column="pf", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "apfc5_data"


class Dg1Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time", primary_key=True
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "dg1_data"


class Dg2Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "dg2_data"


class Dg3Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units"
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "dg3_data"


class Dg4Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "dg4_data"


class Dg5Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time", primary_key=True
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "dg5_data"


class Dg6Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "dg6_data"


class Og1Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "og1_data"


class Og2Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "og2_data"


class Og3Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "og3_data"


class Og4Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "og4_data"


class Og5Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "og5_data"


class Og6Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "og6_data"


class SolFeedData(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "sol_feed_data"


class Tf1Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "tf1_data"


class Tf2Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "tf2_data"


class Tf3Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "tf3_data"


class Tf4Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "tf4_data"


class Tf5Data(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    total_units = models.BigIntegerField(
        db_column="total_units", blank=True, null=True
    )  # Field name made lowercase.
    ll_vltg = models.FloatField(
        db_column="ll_vltg", blank=True, null=True
    )  # Field name made lowercase.
    avg_curr = models.BigIntegerField(
        db_column="avg_curr", blank=True, null=True
    )  # Field name made lowercase.
    r_curr = models.BigIntegerField(
        db_column="r_curr", blank=True, null=True
    )  # Field name made lowercase.
    y_curr = models.BigIntegerField(
        db_column="y_curr", blank=True, null=True
    )  # Field name made lowercase.
    b_curr = models.BigIntegerField(
        db_column="b_curr", blank=True, null=True
    )  # Field name made lowercase.
    act_pwr = models.IntegerField(
        db_column="act_pwr", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "tf5_data"


class WmT0(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(blank=True, null=True)
    final_value = models.IntegerField(blank=True, null=True)

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_t0"


class WmT1(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(blank=True, null=True)
    final_value = models.IntegerField(blank=True, null=True)

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_t1"


class WmT2(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(blank=True, null=True)
    final_value = models.IntegerField(blank=True, null=True)

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_t2"


class WmWm1(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(blank=True, null=True)
    final_value = models.IntegerField(blank=True, null=True)

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm1"


class WmWm2(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm2"


class WmWm3(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm3"


class WmWm4(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm4"


class WmWm5(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm5"


class WmWm6(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm6"


class WmWm7(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm7"


class WmWm8(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm8"


class WmWm9(models.Model):
    date_time = models.DateTimeField(
        db_column="date_time",
        primary_key=True,
    )  # Field name made lowercase.
    initial_value = models.IntegerField(
        db_column="initial_value", blank=True, null=True
    )  # Field name made lowercase.
    final_value = models.IntegerField(
        db_column="final_value", blank=True, null=True
    )  # Field name made lowercase.

    objects = YourCustomManager()

    class Meta:
        managed = True
        db_table = "wm_wm9"
