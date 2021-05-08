from django.shortcuts import render
from Property.models import Property, Category
from django.db.models import Count

# Create your views here.
def home(request):

    category_list = Category.objects.all()
    category_view = Category.objects.annotate(property_count = Count('property')).values('name', 'property_count')
    print(category_view)
    template = 'home.html'
    context = { 
        'category_list' : category_list,
        'category_view' : category_view,
    }
    return render(request, template, context)