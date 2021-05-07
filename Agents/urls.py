from django.urls import path
from Agents import views

app_name = 'Agents'
 
urlpatterns = [
    path('', views.agents_list, name = 'agents_list')
]