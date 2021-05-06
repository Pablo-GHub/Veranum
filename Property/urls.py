from django.urls import path
from Property import views

app_name = 'Property'

urlpatterns = [
    path('', views.property_list, name = 'property_list'),
    path('<int:id>', views.property_detail, name = 'property_detail')
]