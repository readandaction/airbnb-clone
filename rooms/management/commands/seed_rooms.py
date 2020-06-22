import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as rooms_models
from users import models as users_models


class Command(BaseCommand):

    help = "This is my coustom command to create users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default=1, type=int, help="How want me to create users?"
        )

    def handle(self, *args, **options):

        numbers = options.get("numbers")
        seeder = Seed.seeder()
        all_users = users_models.User.objects.all()
        room_types = rooms_models.RoomType.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            numbers,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1, 50),
                "guests": lambda x: random.randint(1, 10),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{numbers} users created"))
