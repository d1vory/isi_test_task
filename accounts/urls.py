from django.urls import path

from accounts.views.registration import RegistrationView

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
]