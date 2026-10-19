from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class HourAccessTests(TestCase):
    def test_non_ta_forbidden(self):
        get_user_model().objects.create_user(username="s", password="pass12345")
        self.client.login(username="s", password="pass12345")
        self.assertEqual(self.client.get(reverse("hour_new")).status_code, 403)