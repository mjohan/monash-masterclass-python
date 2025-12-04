from django.urls import path
from .views.signup import MonashSignupView, SignupSuccessView

app_name = "accounts"

urlpatterns = [
    path("signup/", MonashSignupView.as_view(), name="signup"),
    path("signup/success/", SignupSuccessView.as_view(), name="signup_success"),
]
