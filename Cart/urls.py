from django.urls import path

from .views import Add_Cart, Show_Cart, Update_Cart
from . import views

urlpatterns = [

    path("add-cart/<int:product_id>", Add_Cart, name='Add_Cart'),
    path("Show_Cart/", Show_Cart, name="Show_Cart"),
    path("Update_Cart/<int:product_id>", Update_Cart, name="Update_Cart"),
    path("delete-cart-item/<int:product_id>", views.delete_cart_item, name="delete-cart-item")

]
