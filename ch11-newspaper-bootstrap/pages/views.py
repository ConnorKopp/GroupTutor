from django.views.generic import ListView
from hours.models import TutoringHour

class HomePageView(ListView):
    queryset = TutoringHour.objects.select_related("ta").prefetch_related("ta__courses")
    template_name = "home.html"
    context_object_name = "hour_list"