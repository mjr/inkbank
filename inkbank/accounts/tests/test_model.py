from datetime import datetime

from django.test import TestCase

from ..models import Account


class AccountModelTest(TestCase):
    def setUp(self):
        self.obj = Account(number=12345)
        self.obj.save()

    def test_create(self):
        self.assertTrue(Account.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual("12345", str(self.obj))

    def test_score_default_to_none(self):
        self.assertEqual(None, self.obj.score)
