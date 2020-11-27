from rooms.models import Amenity, Facility
from django.core.management.base import BaseCommand
from rooms import models as room_models

# from rooms.models import Amenity -> 여기서 Amenity만 사용하는게 확실하면 이렇게 해도 되긴함.


class Command(BaseCommand):

    help = "This command creates a lot of facilities"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times?",
        ) """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))