from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from reviews.models import Review


class Command(BaseCommand):

    help = "This is my coustom command to create reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default=2, type=int, help="How want me to create reviews?"
        )

    def handle(self, *args, **options):

        numbers = options.get("numbers")
        seeder = Seed.seeder()
        seeder.add_entity(Review, numbers, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{numbers} users created"))
