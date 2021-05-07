from django.urls import path
from About import views

app_name = 'About'

urlpatterns = [
    path('', views.about_us, name = 'about_us'),
]