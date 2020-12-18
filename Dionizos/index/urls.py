from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("produkt/1",views.produkt, name="produkt"),
]
