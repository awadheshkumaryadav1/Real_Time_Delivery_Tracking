from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 Ye home view dikhega
    path('list/', views.delivery_list, name='delivery_list'),  # optional
]

