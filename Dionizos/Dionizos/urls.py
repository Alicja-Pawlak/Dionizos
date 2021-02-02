
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('verification/', include('verify_email.urls')),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns() 

