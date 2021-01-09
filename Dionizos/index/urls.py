from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path("produkt/<int:pk>/",views.produkt, name="produkt"),
    path('opinie/',views.opinie, name='opinie'),
    path('dodaj/',views.dodaj, name='dodaj')
]

