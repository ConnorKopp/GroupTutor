from django.urls import path
from .views import ProfileUpdateView, SignUpView, TADetailView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("ta/<int:pk>/", TADetailView.as_view(), name="ta_detail"),
    path("profile/", ProfileUpdateView.as_view(), name="profile_edit"),
]
