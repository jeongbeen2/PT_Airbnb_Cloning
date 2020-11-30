from django.shortcuts import render
from . import models

""" #10.1 >> request는, view 함수의 첫번째 인자다. """
""" request가 있어야지만, response가 있다. """


def all_rooms(request):
    """ django에게, all_rooms.html을 comfile하라고 명령하는 것이다. """
    all_rooms = models.Room.objects.all()
    return render(
        request,
        "rooms/home.html",
        context={"rooms": all_rooms},
    )


""" #10.3 >> all_rooms.html => home.html 수정. """

""" templates 파일 이름과, home.html 이름은 반드시 같아야한다. """

""" def name(ex.all_rooms)은 core > urls.py안에 있는 이름과 같아야함. """

""" context의 str부분, (ex. "rooms")는 template 안에서 부를때의 이름이다. """