from math import ceil
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, Paginator
from . import models


""" #10.1 >> request는, view 함수의 첫번째 인자다. """
""" request가 있어야지만, response가 있다. """

""" #11.1 >> request.GET에는 많은 메소드가 들어있고, 그중에 get이라는 메소드를 이용하면 url의 일부를 key, value값으로 가져올수 있다. """
""" 또한, get으로 가져오는 것은 str이기 때문에, int로 바꿔 주어야함. """
""" #11.2 >> 빈 페이지로 갈 경우, 기본값 1을 제공한다. """


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(
        room_list, 10, orphans=5
    )  # orphans -> 끝에 남는애들을 앞페이지에 모조리 보여준다.
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")


""" #11.6 >> Python에서, 에러를 다루는 법은 try & except를 사용해라. 모든경우의 예외는 except Exception 으로 처리. """

""" #10.3 >> all_rooms.html => home.html 수정. """

""" templates 파일 이름과, home.html 이름은 반드시 같아야한다. """

""" def name(ex.all_rooms)은 core > urls.py안에 있는 이름과 같아야함. """

""" context의 str부분, (ex. "rooms")는 template 안에서 부를때의 이름이다. """

""" #11.4 >> dir(rooms.paginator) 안에 page, count 등등 여러메소드가 존재.  """