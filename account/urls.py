from django.urls import path
from .views import SignUpView, LogoutView, SignInView, PasswordResetView, EmailVerificationView, my_profile_view , UpdateMyProfileView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:uidb64>/<str:token>/', EmailVerificationView.as_view(), name='verify_email'),
    path('mypage/<str:accessToken>/', my_profile_view, name='mypage'),
    path('update-profile/<str:accessToken>/', UpdateMyProfileView.as_view(), name='update_profile'),
]