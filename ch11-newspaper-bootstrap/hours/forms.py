from django import forms
from .models import TutoringHour

class HourForm(forms.ModelForm):
    class Meta:
        model = TutoringHour
        fields = ("day", "start_time", "end_time")
        widgets = {
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }