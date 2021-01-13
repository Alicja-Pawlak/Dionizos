from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path("produkt/<int:pk>/",views.produkt, name="produkt"),
    path('opinie/',views.opinie, name='opinie'),
    path('dodaj/',views.dodaj, name='dodaj'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]

