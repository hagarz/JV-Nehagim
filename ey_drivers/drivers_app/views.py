from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Drivers, Schedule


class IndexView(generic.ListView):
    template_name = 'drivers_app/index.html'
    context_object_name = 'driver_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Drivers.objects.all()


class DetailView(generic.DetailView):
    model = Drivers
    template_name = 'drivers_app/detail.html'



def index(request):
    driver_list = Drivers.objects.all()
    context = {'driver_list': driver_list}
    return render(request, 'drivers_app/index.html', context)


def detail(request, driver_id):
    driver = get_object_or_404(Drivers, pk=driver_id)
    return render(request, 'drivers_app/detail.html', {'driver': driver})


def results(request, driver_id):
    response = "You're looking at the results of driver %s."
    return HttpResponse(response % driver_id)

def vote(request, driver_id):
    return HttpResponse("You're voting on question %s." % driver_id)