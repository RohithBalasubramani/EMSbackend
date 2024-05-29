from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import re

class Command(BaseCommand):
    help = 'Converts db_column and db_table string literals in models.py to lowercase.'

    def add_arguments(self, parser):
        # Define a command line argument
        parser.add_argument('app_name', type=str, help='Name of the Django app')

    def handle(self, *args, **options):
        app_name = options['app_name']

        # Locate the app directory within the Django settings
        try:
            app_path = next(
                (os.path.abspath(os.path.join(settings.BASE_DIR, app.split('.')[-1]))
                 for app in settings.INSTALLED_APPS if app.endswith(app_name)),
                None
            )

            if not app_path or not os.path.isdir(app_path):
                raise ValueError("The app path could not be located or is not a directory.")

            models_path = os.path.join(app_path, 'models.py')

            # Check if the models.py file exists
            if not os.path.isfile(models_path):
                raise FileNotFoundError(f"The models.py file could not be found in {app_path}")

            # Read the content of models.py
            with open(models_path, 'r') as file:
                content = file.read()

            # Function to convert matched strings to lowercase
            def to_lowercase(match):
                return f'{match.group(1)}"{match.group(2).lower()}"'

            # Combined regex to target both db_column and db_table values
            updated_content = re.sub(r'(db_column=|db_table = )"([^"]+)"', to_lowercase, content)

            # Write the updated content back to models.py
            with open(models_path, 'w') as file:
                file.write(updated_content)

            self.stdout.write(self.style.SUCCESS(f'Successfully converted db_column and db_table string literals to lowercase in {models_path}'))

        except ValueError as ve:
            self.stdout.write(self.style.ERROR(str(ve)))
        except FileNotFoundError as fnfe:
            self.stdout.write(self.style.ERROR(str(fnfe)))
        except Exception as e:
            raise CommandError(f'An error occurred: {str(e)}')
