from django.shortcuts import render
from .models import Property, Category, Reserve
from .forms import ReserveForm
# Create your views here.
def property_list(request):

    property_list = Property.objects.all()
    template = 'list.html'
    context = {
        'property_list' : property_list
    }

    return render(request, template, context)

def property_detail(request, id):

    property_detail = Property.objects.get(id=id)
    template = 'detail.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserveForm()

    context = {
        'property_detail' : property_detail,
        'reserve_form' : reserve_form
    }

    return render(request, template, context)