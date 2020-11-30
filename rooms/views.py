from django.shortcuts import render

""" #10.1 >> request는, view 함수의 첫번째 인자다. """
""" request가 있어야지만, response가 있다. """


def all_rooms(request):
    return render(request, "all_rooms")