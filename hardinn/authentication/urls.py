from django.urls import path
from  .views import CustomLoginView
from hardinn.views import  index


urlpatterns = [


     path("login/",CustomLoginView.as_view(),name="login"),
      path('', index, name="home"),
]
