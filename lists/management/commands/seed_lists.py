import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from lists import models as lists_models
from rooms import models as rooms_models
from users import models as users_models

NAME = "lists"


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
            lists_models.List, numbers, {"user": lambda x: random.choice(users),}
        )
        created_lists = seeder.execute()
        cleaned = flatten(list(created_lists.values()))
        for pk in cleaned:
            list_model = lists_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{numbers} {NAME} created"))
