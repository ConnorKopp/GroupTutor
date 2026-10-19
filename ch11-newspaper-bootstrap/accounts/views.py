from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import CustomUserCreationForm, TAProfileForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class TADetailView(DetailView):
    model = CustomUser
    template_name = "ta_detail.html"
    context_object_name = "ta"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TAProfileForm
    template_name = "profile_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user