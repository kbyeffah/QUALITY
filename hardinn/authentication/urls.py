from django.urls import path
from  .views import CustomLoginView
from hardinn.views import  index
from  .views import CustomRegisterView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView

urlpatterns = [
     path('', index, name="home"),
     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
     path("login/",CustomLoginView.as_view(),name="login"),
     path("register/",CustomRegisterView.as_view(),name="register"),
     # path("accounts/login/",CustomLoginView.as_view(),name="login"),
     # path('login/', RedirectView.as_view(url = '/accounts/login'), name = "login")
  
]

