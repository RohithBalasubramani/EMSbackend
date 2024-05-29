class AnomalyDatabaseRouter:
    def db_for_read(self, model, **hints):
        return "default"  # Use the 'default' database for other models

    def db_for_write(self, model, **hints):
        # Route all write operations to the default database
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        # Decide if relations between objects should be allowed
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Decide if a migration operation should be allowed on a database
        return True
