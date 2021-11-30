from django.shortcuts import render
from django.http import Http404
from .models import Owner, Car
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
import datetime
from .models import Owner
from .models import OwnerForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def detail(request, id_owner):
    try:
        p = Owner.objects.get(pk=id_owner)
    except Owner.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'project_first_app/owner.html', {'Owner': p})

def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = Owner.objects.all()
    return render(request, "project_first_app/owner_view.html", context)

class CarView(DetailView):
    model = Car

class CarListView(ListView):
    model = Car
    queryset = model.objects.all()


def create_owner(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "project_first_app/create_owner.html", context)

class CarUpdateView(UpdateView):
  model = Car
  fields = ['number_plate', 'car_brand', 'car_model', 'car_color']
  success_url = '/car/list/'

class CarCreateView(CreateView):
  model = Car
  fields = ['number_plate', 'car_brand', 'car_model', 'car_color']
  success_url = '/car/list/'

class CarDeleteView(DeleteView):
  model = Car
  success_url = '/car/list/'
