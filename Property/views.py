from django.shortcuts import render
from .models import Property, Category, Reserve
from .forms import ReserveForm
from django.db.models import Q

# Create your views here.
def property_list(request):

    property_list = Property.objects.all()
    template = 'list.html'

    address_query = request.GET.get('search')
    property_type_query = request.GET.getlist('property_type', None)
    if address_query and property_type_query:
        property_list = property_list.filter(
            Q(name__icontains = address_query) &
            Q(property_type__icontains = property_type_query[0]) |
            Q(location__icontains = address_query)
        )
    
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