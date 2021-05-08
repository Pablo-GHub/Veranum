from django.shortcuts import render
from Property.models import Property, Category
from django.db.models import Count

# Create your views here.
def home(request):

    category_list = Category.objects.annotate(count = Count('property')).values('name', 'count', 'image')
    print(category_list)
    template = 'home.html'
    context = { 
        'category_list' : category_list,
    }
    return render(request, template, context)