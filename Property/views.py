from django.shortcuts import render
from .models import Property, Category
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
    context = {
        'property_detail' : property_detail
    }

    return render(request, template, context)