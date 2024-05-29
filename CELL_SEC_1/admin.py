from django.contrib import admin
from django.apps import apps

# Get all models from your app
app_models = apps.get_app_config("CELL_SEC_1").get_models()


# Custom admin class to dynamically display all fields
class DynamicFieldsAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)


# Register all models with the custom admin class
for model in app_models:
    admin.site.register(model, DynamicFieldsAdmin)


# Register your models here.
