from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

class Command(BaseCommand):
    help = "Creates an initial superuser if it does not exist"

    def handle(self, *args, **options):
        User = get_user_model()
        username = getattr(settings, "ADMIN_USERNAME", "admin")
        email = getattr(settings, "ADMIN_EMAIL", "admin@example.com")
        password = getattr(settings, "ADMIN_PASSWORD", "adminpassword123")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))

