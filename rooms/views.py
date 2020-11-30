from datetime import date, datetime
from django.shortcuts import render

""" #10.1 >> request는, view 함수의 첫번째 인자다. """
""" request가 있어야지만, response가 있다. """


def all_rooms(request):
    """ django에게, all_rooms.html을 comfile하라고 명령하는 것이다. """
    now = datetime.now()
    hungry = False
    return render(
        request,
        "all_rooms.html",
        context={
            "now": now,
            "hungry": hungry,
        },
    )
