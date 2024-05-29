from django.core.management.base import BaseCommand
from statistics import median
from PEPPL_DATA.models import Amf1DailyKwh
from Anomaly.models import Amf1DailyKwhAnomalyTest


class Command(BaseCommand):
    help = "Run the anomaly detection algorithm"

    def handle(self, *args, **kwargs):
        model = Amf1DailyKwh  # Set the model for which anomalies need to be detected

        # Calculate the median value for each field in the Amf1DailyKwh model
        fields_to_calculate = [
            "tf2_kwh",
            "og2_kwh",
            "og1_kwh",
            "tf1_kwh",
        ]

        median_values = {}
        for field in fields_to_calculate:
            values = model.objects.values_list(field, flat=True)
            median_value = median(values)
            median_values[field] = median_value
            print(f"Median value for {field}: {median_value}")

        # Find anomalies based on specific conditions and categorize them
        anomalies = []
        for record in model.objects.all():
            for field in fields_to_calculate:
                value = getattr(record, field)

                # Check if 'value' is negative
                if value and value < 0:
                    anomalies.append(
                        {
                            "instance": record,
                            "field": field,
                            "value": value,
                            "median_value": median_values[field],
                            "reason": f"Anomaly detected: Negative value ({field})",
                        }
                    )
                    break  # Move to the next record after finding a negative anomaly in a column

                # Check if 'value' in any column is 3 times the median value of the corresponding column
                elif value and value > 3 * median_values[field]:
                    anomalies.append(
                        {
                            "instance": record,
                            "field": field,
                            "value": value,
                            "median_value": median_values[field],
                            "reason": f"Anomaly detected: Value much higher than the median ({field})",
                        }
                    )
                    break  # Move to the next record after finding an anomaly in a column

                # Check if 'tf1_kwh' is not equal to 'og1_kwh' or 'tf2_kwh' is not equal to 'og2_kwh'
                elif (record.tf1_kwh != record.og1_kwh) or (
                    record.tf2_kwh != record.og2_kwh
                ):
                    anomalies.append(
                        {
                            "instance": record,
                            "field": None,
                            "value": None,
                            "median_value": None,
                            "reason": "Anomaly detected: Transformer Not Equal to Outgoing",
                        }
                    )
                    break  # Move to the next record after finding an anomaly in a column

        # Store anomalies in the Amf1DailyKwhAnomalyTest model
        for anomaly in anomalies:
            Amf1DailyKwhAnomalyTest.objects.create(
                date_time=anomaly["instance"].date_time,
                apfc2_kwh_anomaly=anomaly["instance"].apfc2_kwh,
                tf2_kwh_anomaly=anomaly["instance"].tf2_kwh,
                dg2_kwh_anomaly=anomaly["instance"].dg2_kwh,
                og2_kwh_anomaly=anomaly["instance"].og2_kwh,
                og1_kwh_anomaly=anomaly["instance"].og1_kwh,
                dg1_kwh_anomaly=anomaly["instance"].dg1_kwh,
                tf1_kwh_anomaly=anomaly["instance"].tf1_kwh,
                apfc1_kwh_anomaly=anomaly["instance"].apfc1_kwh,
                reason=anomaly["reason"],
            )
