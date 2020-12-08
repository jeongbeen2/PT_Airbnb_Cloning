from django.core import paginator
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
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


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)
                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms}
                )
        else:
            """ #13.10 >> url에 문제가 있다면, else로 넘어와서 빈 페이지의 form을 render한다. """
            """ 문제가 없다면, form.is_valid에 있는 filter 기능을 잘 사용한다. """
            """ url을 제멋대로 바꾸면, 장고가 알아서 해결해줌. """
            """ ex, room_type의 pk는 4까지지만, 123431531 이렇게 치면 에러메세지를 대신 띄워준다. """

            form = forms.SearchForm()
        return render(request, "rooms/search.html", {"form": form})
