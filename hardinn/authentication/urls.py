from django.urls import path
from  .views import CustomLoginView
from hardinn.views import  index
from  .views import CustomRegisterView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView
from django.urls import path, include

urlpatterns = [
     path('index', index, name="home"),
     # path("logout/", LogoutView.as_view(next_page="logout"), name="logout"),
     path("login/",CustomLoginView.as_view(),name="login"),
     path('login/', RedirectView.as_view(url = 'login'), name = "logout"),
     path("register/",CustomRegisterView.as_view(),name="register"),
     path('',include('django.contrib.auth.urls')),
     path("accounts/login/",CustomLoginView.as_view(),name="login"),
    
     path('verification/', include('verify_email.urls')),
] 