from django.core.management.base import BaseCommand

""" #9.0>> 원하는 app폴더 내에, management > commands 폴더를 만들어주고, __init__.py를 만들어 이 폴더가 파이썬 폴더라는것을 장고에게 알려준다. """

""" BaseCommand를 import 해준다. """
""" add_arguments, handle을 만들어주고, 원하는 커맨드를 적는다. """
""" ex) python manage.py loveyou --times 50 실행시키기. """


class Command(BaseCommand):

    help = "This command is hello"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times?",
        )

    def handle(self, *args, **options):
        times = options.get(
            "times"
        )  # --times 50 이라는 코드를 실행시키기 위해, loveyou(self) --times(*args) 50(**options) 를 가져옴.
        for t in range(0, int(times)):  # times == 50이기 때문에, 50번 실행을 하게 된다.
            self.stdout.write(self.style.WARNING("heelloo~"))
