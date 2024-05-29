# myapp/cron.py

from django_cron import CronJobBase, Schedule
from statistics import median
from PEPPL_DATA.models import Amf1DailyKwh
from .models import (
    Amf1DailyKwhAnomalies,
)  # Adjust this import based on your app structure


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ["20:30"]
    schedule = Schedule(run_every_mins=RUN_AT_TIMES)
    code = "AnomalyDetection.my_cron_job"  # A unique code

    def do(self):
        # Your anomaly detection logic here
        model = Amf1DailyKwh  # Set the model for which anomalies need to be detected

        # Calculate the median value for the Amf1DailyKwh model
        values = model.objects.values_list("value", flat=True)
        median_value = median(values)

        # Find anomalies based on specific conditions and categorize them
        anomalies = []
        for anomaly in model.objects.all():
            anomaly_type = None

            if anomaly.value > 2 * median_value:
                anomaly_type = "Values greater than double the median"
            elif anomaly.value < 0:
                anomaly_type = "Negative values"
            elif anomaly.tf1 != anomaly.og1 or anomaly.tf2 != anomaly.og2:
                anomaly_type = "Specific field inequality"

            if anomaly_type:
                anomalies.append(
                    {
                        "instance": anomaly,
                        "type": anomaly_type,
                    }
                )

        # Store anomalies in the Amf1DailyKwhAnomalies model
        for anomaly in anomalies:
            Amf1DailyKwhAnomalies.objects.create(
                value=anomaly["instance"].value,
                reason=f"Anomaly detected: {anomaly['type']}",
                timestamp=anomaly["instance"].timestamp,
                # Add other fields specific to your Amf1DailyKwhAnomalies model
            )
