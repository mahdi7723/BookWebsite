from django.urls import path
from books import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('author/<int:author_id>/', views.author_book, name='author'),
]
