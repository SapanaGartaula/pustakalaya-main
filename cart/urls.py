from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add_tocart/<int:book_id>/", views.add_to_cart, name='add_to_cart'),
    path("remove_cart/<str:book_id>/<str:cart_item_id>/", views.remove_cart_book, name='remove_cart'),
    path("decrement_cart_item/<str:book_id>/<str:cart_item_id>/", views.decrement_cart_item, name='decrement_cart_item'),
    path("increment_cart_item/<str:book_id>/<str:cart_item_id>/", views.increment_cart_item, name='increment_cart_item'),
    path('checkout/',views.checkout, name='checkout'),
    path('payment/',views.payment, name='payment'),
]   