from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views
from .views import token_send,success,error_page,verify

urlpatterns = [
    path("register/", users_views.register, name='register'),
    path('settings/', users_views.profile, name='settings'),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('token_send/' , users_views.token_send , name="token_send"),
    path('success/' , users_views.success , name='success'),
    path('verify/<auth_token>' , users_views.verify , name="verify"),
    path('error' ,users_views. error_page , name="error"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete')
]