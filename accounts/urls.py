from django.urls import path

from .views import login_view, signup_view, forgot_password_view

urlpatterns = [
    path('', login_view,name='accounts-page'),
    path('login', login_view, name='login-page'),
    path('signup', signup_view, name='signup-page'),
    path('forgot', forgot_password_view, name='forgot-password-page')
]