from . import views
from django.urls import path
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.UserLoginView.as_view(
        template_name="registration/login.html"), name="login"),
    path("register/", views.UserRegister.as_view(), name="register"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),

    #password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    path("change-password/<uuid:uuid>", views.UserPasswordChange.as_view(),name="change-password")
]
