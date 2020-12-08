from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django_countries import countries
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})
