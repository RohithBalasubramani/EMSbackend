from django.core.management.base import BaseCommand
from statistics import median
from PEPPL_DATA.models import Amf2DailyKwh
from Anomalydb.models import Amf2DailyKwhAnomalyDb  # Updated model name


class Command(BaseCommand):
    help = "Run the anomaly detection algorithm for Amf2DailyKwh model"

    def handle(self, *args, **kwargs):
        model = Amf2DailyKwh  # Set the model for which anomalies need to be detected

        # Calculate the median value for each field in the Amf2DailyKwh model
        fields_to_calculate = [
            "tf4_kwh",
            "og4_kwh",
            "og3_kwh",
            "tf3_kwh",
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

                # Check if 'tf3_kwh' is not equal to 'og3_kwh' or 'tf4_kwh' is not equal to 'og4_kwh'
                elif (record.tf3_kwh != record.og3_kwh) or (
                    record.tf4_kwh != record.og4_kwh
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

        # Store anomalies in the Amf2DailyKwhAnomalyDb model
        for anomaly in anomalies:
            Amf2DailyKwhAnomalyDb.objects.create(
                date_time=anomaly["instance"].date_time,
                apfc4_kwh_anomaly=anomaly["instance"].apfc4_kwh,
                tf4_kwh_anomaly=anomaly["instance"].tf4_kwh,
                dg4_kwh_anomaly=anomaly["instance"].dg4_kwh,
                og4_kwh_anomaly=anomaly["instance"].og4_kwh,
                og3_kwh_anomaly=anomaly["instance"].og3_kwh,
                dg3_kwh_anomaly=anomaly["instance"].dg3_kwh,
                tf3_kwh_anomaly=anomaly["instance"].tf3_kwh,
                apfc3_kwh_anomaly=anomaly["instance"].apfc3_kwh,
                reason=anomaly["reason"],
            )
