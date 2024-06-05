from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

class Command(BaseCommand):
    help = 'Create a custom superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username=config('ADMIN_USERNAME'),
                email=config('ADMIN_EMAIL'),
                password=config('ADMIN_PASSWORD'),
            )
            self.stdout.write(self.style.SUCCESS('Successfully created new superuser'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
