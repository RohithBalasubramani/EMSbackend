class MyDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "MOD_SEC_1":
            return "read_only_db2"  # Route read operations for app1 models to read-only DB1
        # Route other read operations to the default database
        return "default"

    def db_for_write(self, model, **hints):
        # Route all write operations to the default database
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        # Decide if relations between objects should be allowed
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Decide if a migration operation should be allowed on a database
        return True
