from django.urls import path
from Contact import views

app_name = 'Contact'

urlpatterns = [
    path('', views.send_mail, name = 'send_mail'),
    path('success/', views.success, name = 'success'),
]