from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.
from .models import Tweet

User = get_user_model()

class TWeetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username="Clare222222")

    def test_tweet_item(self):
        obj = Tweet.objects.create(user=User.objects.first(), content="Some test message.")
        self.assertTrue(obj.content == "Some test message.")
        self.assertTrue(obj.id == 1)

    def test_tweet_url(self):
        obj = Tweet.objects.create(user=User.objects.first(), content="Some test message.")
        absoulte_url = reverse("tweet:detail", kwargs={"pk": obj.pk})
        self.assertEqual(obj.get_absolute_url(), absoulte_url)
