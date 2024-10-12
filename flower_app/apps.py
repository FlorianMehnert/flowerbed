from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError


class FlowerAppConfig(AppConfig):
    name = 'flower_app'

    def ready(self):
        # Import the User model only after the registry is ready
        from django.contrib.auth.models import User

        try:
            if not User.objects.filter(username='florian').exists():
                User.objects.create_superuser(
                    username='florian',
                    email='florian.mehnert@gmail.com',
                    password='florian'
                )
                print("Admin user created.")
        except (OperationalError, ProgrammingError):
            # Catch errors related to the database not being ready
            print("Database not ready, skipping admin creation.")
