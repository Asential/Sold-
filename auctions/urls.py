from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("wishlist/<int:id>", views.wishlist, name="wishlist"),
    path("unwishlist/<int:id>", views.unwishlist, name="unwishlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("placebid/<int:id>", views.placebid, name="placebid"),
    path("save", views.save, name="save"),
    path("listing/<int:id>", views.listing, name="listing")
]
