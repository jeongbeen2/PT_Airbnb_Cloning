# from django.shortcuts import redirect, render
# from django.core.paginator import EmptyPage, Paginator
from django.utils import timezone
from django.views.generic import ListView
from . import models
from django.shortcuts import render


""" #10.1 >> request는, view 함수의 첫번째 인자다. """
""" request가 있어야지만, response가 있다. """

""" #11.1 >> request.GET에는 많은 메소드가 들어있고, 그중에 get이라는 메소드를 이용하면 url의 일부를 key, value값으로 가져올수 있다. """
""" 또한, get으로 가져오는 것은 str이기 때문에, int로 바꿔 주어야함. """
""" #11.2 >> 빈 페이지로 갈 경우, 기본값 1을 제공한다. """

""" #11.7 >> HomeView """


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"
    """ #11.7 >> ccbv를 통해, ListView의 모든것을 볼 수 있음. """
    """ https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/ """
    context_object_name = "rooms"  # #11.8 >> object_list -> 이름을 바꿀수 있다.


""" #12.0 >> pk라는 인자는, rooms/@ -> @안의 숫자를 가져온다. """


def room_detail(request, pk):
    return render(request, "rooms/detail.html")

    """ #11.8 >> get_context_data로, CBV를 커스텀할수 있다. """
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     """ context는, 내가 만들었던 것들이다. (ex. room list들.) """
    #     now = timezone.now()
    #     context["now"] = now
    #     return context


# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(
#         room_list, 10, orphans=5
#     )  # orphans -> 끝에 남는애들을 앞페이지에 모조리 보여준다.
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")


""" #11.6 >> Python에서, 에러를 다루는 법은 try & except를 사용해라. 모든경우의 예외는 except Exception 으로 처리. """

""" #10.3 >> all_rooms.html => home.html 수정. """

""" templates 파일 이름과, home.html 이름은 반드시 같아야한다. """

""" def name(ex.all_rooms)은 core > urls.py안에 있는 이름과 같아야함. """

""" context의 str부분, (ex. "rooms")는 template 안에서 부를때의 이름이다. """

""" #11.4 >> dir(rooms.paginator) 안에 page, count 등등 여러메소드가 존재.  """