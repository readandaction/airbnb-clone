import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from rooms.models import Room
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
        all_users = User.objects.all()
        all_rooms = Room.objects.all()
        seeder.add_entity(
            Review,
            numbers,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleaniness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "user": lambda x: random.choice(all_users),
                "room": lambda x: random.choice(all_rooms),
            },
        )
        created_reviews = seeder.execute()
        clean_review = flatten(list(created_reviews.values()))
        print(clean_review)

        self.stdout.write(self.style.SUCCESS(f"{numbers} reviews created"))
