from django.urls import path
from .views import index, destination_detail, profile,  \
    profile, Register, ProfileUpdate
from django.contrib.auth.views import LoginView, LogoutView

app_name='course'

urlpatterns = [
    path('', index, name='destination_list'),
    path('<slug:slug>', destination_detail, name='destination_detail'),


    # Profile and Auth
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', ProfileUpdate.as_view(), name='profile_update'),
]