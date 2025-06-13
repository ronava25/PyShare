from django.urls import path, reverse_lazy
from .views import profile_view, ProfileUpdateView, UserLoginView, UserLogoutView, UserRegisterView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]
