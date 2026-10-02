from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("collection/", views.CollectionView.as_view(), name="collection"),
    path("collection/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("custom-orders/", views.CustomOrdersView.as_view(), name="custom_orders"),
    path("our-story/", views.OurStoryView.as_view(), name="our_story"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("cart/", views.CartView.as_view(), name="cart"),
]
