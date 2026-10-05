from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('cart/', views.cart_detail, name='cart'),
    path('cart/detail/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:game_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.my_orders, name='my_orders'),
    path('library/', views.my_library, name='library'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('lang/<str:code>/', views.set_language, name='set_language'),
    path('buy/<int:game_id>/', views.buy_now, name='buy_now'),
    path('settings/', views.settings_page, name='settings'),
    path('wishlist/toggle/<int:game_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('game/<int:game_id>/review/', views.add_review, name='add_review'),
    path('profile/', views.profile_view, name='profile'),
]