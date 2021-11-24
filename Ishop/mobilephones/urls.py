from django.urls import path

from . import views

app_name = 'mobiles'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('group/<slug:slug>/', views.get_list, name = 'get_list')
]