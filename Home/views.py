from django.shortcuts import render
from Property.models import Property, Category

# Create your views here.
def home(request):

    category_list = Category.objects.all()
    template = 'home.html'
    context = {
        'category_list' : category_list,
    }
    return render(request, template, context)