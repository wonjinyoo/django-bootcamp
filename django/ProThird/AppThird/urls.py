from django.urls import path
from AppThird import views

urlpatterns = [
    path('', views.users, name='users')
]
