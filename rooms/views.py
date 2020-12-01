from django.shortcuts import render
from . import models


""" #10.1 >> request는, view 함수의 첫번째 인자다. """
""" request가 있어야지만, response가 있다. """

""" #11.1 >> request.GET에는 많은 메소드가 들어있고, 그중에 get이라는 메소드를 이용하면 url의 일부를 key, value값으로 가져올수 있다. """
""" 또한, get으로 가져오는 것은 str이기 때문에, int로 바꿔 주어야함. """


def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={"rooms": all_rooms},
    )


""" #10.3 >> all_rooms.html => home.html 수정. """

""" templates 파일 이름과, home.html 이름은 반드시 같아야한다. """

""" def name(ex.all_rooms)은 core > urls.py안에 있는 이름과 같아야함. """

""" context의 str부분, (ex. "rooms")는 template 안에서 부를때의 이름이다. """