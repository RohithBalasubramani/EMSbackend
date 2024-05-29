class MyDBRouter:
    def db_for_read(self, model, **hints):
        """
        Route read operations for PEPPL_DATA models to read_only_db1.
        """
        if model._meta.app_label == "PEPPL_DATA":
            return "read_only_db1"
        return "default"

    def db_for_write(self, model, **hints):
        """
        Route write operations for PEPPL_DATA models to postgres_db.
        """
        if model._meta.app_label == "PEPPL_DATA":
            return "postgres_db"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the PEPPL_DATA app is involved.
        """
        if obj1._meta.app_label == "PEPPL_DATA" or obj2._meta.app_label == "PEPPL_DATA":
            return True
        return None  # Returning None means use the default behavior

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the PEPPL_DATA app's migrations only run on postgres_db.
        """
        if app_label == "PEPPL_DATA":
            return db == "postgres_db"
        return None  # Returning None means all other apps can migrate as per the default rules
