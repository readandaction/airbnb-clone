from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This is my coustom command no.1"

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How want me to tell you I love you?")

    def handle(self, *args, **options):
        print(args, options)
        print("hello")
        times = options.get("times")
        for t in range(0, int(times)):
            print("love", t)
            self.stdout.write(self.style.SUCCESS("green"))
            self.stdout.write(self.style.WARNING("Yellow"))
