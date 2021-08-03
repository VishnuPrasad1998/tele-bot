from django.test import TestCase
from .models import Buttonhits
from django.contrib.auth.models import User
# Create your tests here.

class ButtonhitsTestCase(TestCase):
	def setUp(self):
		user1 = User.objects.create(email="user1@gmail.com", first_name="User", last_name="One", username='user1', password="Abcd1234#")
		Buttonhits.objects.create(user=user1)
		user2 = User.objects.create(email="user2@gmail.com", first_name="User", last_name="Two", username='user2', password="Abcd1234#")
		Buttonhits.objects.create(user=user2, fat_hits=0, dumb_hits=2, stupid_hits=3)

	def test_button_hits(self):
		"""Test to verify button hits"""
		user1 = Buttonhits.objects.get(user=1)
		user2 = Buttonhits.objects.get(user=2)
		self.assertEqual(user1.fat_hits, 0)
		self.assertEqual(user2.stupid_hits, 3)
