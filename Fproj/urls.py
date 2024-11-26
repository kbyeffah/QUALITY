from django.urls import path
from  .views import CustomLoginView
from .views import home



urlpatterns = [

    path("login/",CustomLoginView.as_view(),name="login"),
    path('', home, name="home"),
]

