from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import HourForm

class HourCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = HourForm
    template_name = "hour_new.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_ta

    def form_valid(self, form):
        form.instance.ta = self.request.user
        return super().form_valid(form)