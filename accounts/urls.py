from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import EditProfile


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/<int:user_id>/', views.Profile, name='profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),
]
