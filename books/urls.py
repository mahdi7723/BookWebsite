from django.urls import path
from books import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('author/<int:author_id>/', views.author_book, name='author'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),

]
