from django.conf import settings
from django.db import models

class TutoringHour(models.Model):
    DAY_CHOICES = [
        (0, "Monday"), (1, "Tuesday"), (2, "Wednesday"),
        (3, "Thursday"), (4, "Friday"),
    ]
    ta = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="hours",
    )
    day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ["day", "start_time"]

    def __str__(self):
        return f"{self.ta} {self.get_day_display()} {self.start_time}-{self.end_time}"