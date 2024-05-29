from django.db import models


class Amf1DailyKwhAnomalyTest(models.Model):
    date_time = models.DateTimeField(primary_key=True)
    apfc2_kwh_anomaly = models.FloatField(blank=True, null=True)
    tf2_kwh_anomaly = models.FloatField(blank=True, null=True)
    dg2_kwh_anomaly = models.FloatField(blank=True, null=True)
    og2_kwh_anomaly = models.FloatField(blank=True, null=True)
    og1_kwh_anomaly = models.FloatField(blank=True, null=True)
    dg1_kwh_anomaly = models.FloatField(blank=True, null=True)
    tf1_kwh_anomaly = models.FloatField(blank=True, null=True)
    apfc1_kwh_anomaly = models.FloatField(blank=True, null=True)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"Anomaly for Amf1DailyKwh at {self.date_time}: {self.reason}"


class Amf2DailyKwhAnomalyTest(models.Model):
    date_time = models.DateTimeField(primary_key=True)
    apfc4_kwh_anomaly = models.FloatField(blank=True, null=True)
    tf4_kwh_anomaly = models.FloatField(blank=True, null=True)
    dg4_kwh_anomaly = models.FloatField(blank=True, null=True)
    og4_kwh_anomaly = models.FloatField(blank=True, null=True)
    og3_kwh_anomaly = models.FloatField(blank=True, null=True)
    dg3_kwh_anomaly = models.FloatField(blank=True, null=True)
    tf3_kwh_anomaly = models.FloatField(blank=True, null=True)
    apfc3_kwh_anomaly = models.FloatField(blank=True, null=True)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"Anomaly for Amf2DailyKwh at {self.date_time}: {self.reason}"
