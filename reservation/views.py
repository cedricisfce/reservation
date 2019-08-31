from django.shortcuts import render
from reservation.models import Shows
from reservation import navigation

# Create your views here.
def shows_list(request):
    shows = Shows.objects.all()
    contexte = {
        'navigation_items': navigation.navigation_items(navigation.NAV_SHOWS),
        'shows': shows,
    }
    return render(request, 'reservation/shows_list.html', contexte)

