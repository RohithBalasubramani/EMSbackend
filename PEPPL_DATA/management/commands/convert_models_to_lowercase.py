from django.core.management.base import BaseCommand
from django.apps import apps
import os

class Command(BaseCommand):
    help = 'Convert db_table and db_column names to lowercase'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the app to convert models for')

    def handle(self, *args, **options):
        app_name = options['app_name']
        app_models = apps.get_app_config(app_name).get_models()
        output_lines = []

        for model in app_models:
            output_lines.append(f'class {model.__name__}(models.Model):')
            
            for field in model._meta.fields:
                field_line = f'    {field.name} = models.{field.__class__.__name__}('
                field_params = [f'db_column=\'{field.db_column.lower() if field.db_column else field.name.lower()}\'' + (', ' if not field.primary_key else '')]

                if field.null:
                    field_params.append('null=True')
                if field.blank:
                    field_params.append('blank=True')
                if field.has_default():
                    default = field.get_default()
                    default = f"'{default}'" if isinstance(default, str) else str(default)
                    field_params.append(f'default={default}')
                # Include other field parameters as necessary

                field_line += ', '.join(field_params) + ')'
                output_lines.append(field_line)

            db_table = model._meta.db_table.lower() if model._meta.db_table else model._meta.model_name.lower()
            output_lines.append('    class Meta:')
            output_lines.append(f'        db_table = \'{db_table}\'')
            output_lines.append('')  # Empty line for readability

        output_file_path = os.path.join('/home/rohithbalasubramani/myprojectdir', f'{app_name}_lowercase_models.py')  # Replace with your desired path
        with open(output_file_path, 'w') as file:
            file.write('\n'.join(output_lines))

        self.stdout.write(self.style.SUCCESS(f'Model definitions converted successfully. Check the file {output_file_path}'))
