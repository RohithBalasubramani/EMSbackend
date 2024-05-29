from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction


class Command(BaseCommand):
    help = "Syncs data from read_only_db2 to postgres_db_mod1 for all models in a specified app"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--appname",
            type=str,
            help="Specify the app name to sync data for",
        )

    def handle(self, *args, **options):
        app_name = options["appname"]
        if not app_name:
            self.stdout.write(
                self.style.ERROR("Please specify an app name using --appname")
            )
            return

        # Get all models for the specified app
        models = apps.get_app_config(app_name).get_models()

        for model in models:
            self.stdout.write(f"Processing {model.__name__}...")

            with transaction.atomic(using="postgres_db_mod1"):
                # Fetch all objects from read_only_db2
                objects = model.objects.using("read_only_db2").all()

                for obj in objects:
                    # Use model's pk attribute name to fetch the primary key
                    pk_name = model._meta.pk.attname
                    pk_value = getattr(obj, pk_name)

                    # Create a dict of all field values to update or create
                    data = {
                        field.name: getattr(obj, field.name)
                        for field in model._meta.fields
                    }

                    # Update or create the object in postgres_db_mod1
                    model.objects.using("postgres_db_mod1").update_or_create(
                        defaults=data, **{pk_name: pk_value}
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully synced {model.__name__} to postgres_db_mod1"
                )
            )
