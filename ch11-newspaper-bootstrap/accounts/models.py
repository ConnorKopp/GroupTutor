from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)  

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return self.code

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    is_ta = models.BooleanField("I am a TA", default=False)  
    bio = models.TextField(blank=True)  
    courses = models.ManyToManyField(Course, blank=True)  

    def get_absolute_url(self):  
        return reverse("ta_detail", kwargs={"pk": self.pk})