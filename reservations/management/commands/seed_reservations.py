import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservations_models
from rooms import models as rooms_models
from users import models as users_models

NAME = "reservations"


class Command(BaseCommand):

    help = f"This is my coustom command to create {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default=1, type=int, help=f"How want me to create {NAME}?"
        )

    def handle(self, *args, **options):

        numbers = options.get("numbers")
        users = users_models.User.objects.all()
        rooms = rooms_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            reservations_models.Reservation,
            numbers,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} {NAME} created"))
