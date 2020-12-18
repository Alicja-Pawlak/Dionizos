from django.urls import path
from . import views


urlpatterns = [
    path('',views.opinie,name='opinie'),
]
