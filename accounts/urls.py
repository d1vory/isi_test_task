from django.urls import path

from accounts.views.login import LoginView
from accounts.views.registration import RegistrationView

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
]