from django.core.management.base import BaseCommand
from rooms.models import Facility

# from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This is my coustom command to create seed_facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for facility in facilities:
            Facility.objects.create(name=facility)

        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created"))

