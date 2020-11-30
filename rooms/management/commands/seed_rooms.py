import random
from random import seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    """ #9.3 >> 방을 만들기위해서는, host와 room_type이 필수라고 지정해줬으므로, 아래와같이 add_entity로 직접 지정해줘야한다. """
    """ faker는 django_seed에서 좋은 기능 중 하나임. """

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "guests": lambda x: random.randint(0, 4),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(50, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        """ #9.4 >> flatten은, [[13]] 과 같은 형식을 [13]으로 바꿔준다. """
        """ 만들어진 방의 넘버를 primary key, pk로 지정하고, 그 방안에 3~17개의 사진을 넣어주는 과정임. """
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                )
            """ #9.5 >> Many To Many Field에서 새로운 것을 추가할 때, 0~15의 숫자를 뽑아 그중 2로 나누어진다면 추가하는 방법. """
            """ 많이 쓰는 방식이다. """
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))