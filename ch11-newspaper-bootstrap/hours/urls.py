from django.urls import path
from .views import HourCreateView

urlpatterns = [
    path("new/", HourCreateView.as_view(), name="hour_new"),
]