# from django.contrib import admin
# from django.apps import apps

# # Get all models from your app
# app_models = apps.get_app_config("Anomaly").get_models()


# # Custom admin class to dynamically display all fields and add filter by 'reason'
# class DynamicFieldsAdmin(admin.ModelAdmin):
#     def __init__(self, model, admin_site):
#         self.list_display = [
#             field.name for field in model._meta.fields if field.name != "id"
#         ]
#         self.list_filter = ("reason",)  # Filter by 'reason' field
#         super().__init__(model, admin_site)


# # Register all models with the custom admin class
# for model in app_models:
#     admin.site.register(model, DynamicFieldsAdmin)
