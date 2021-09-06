from datetime import datetime

from django.test import TestCase

from ..models import Account


class AccountSimpleTest(TestCase):
    def setUp(self):
        self.obj = Account(number=12345)
        self.obj.save()

    def test_deposit(self):
        self.obj.deposit(10)
        self.assertEqual(self.obj.balance, 10)

    def test_withdraw(self):
        self.obj.deposit(10)
        self.obj.withdraw(5)
        self.assertEqual(self.obj.balance, 5)

    def test_transfer(self):
        receiver = Account(number=67890)
        self.obj.deposit(10)
        self.obj.transfer(receiver, 5)
        self.assertEqual(self.obj.balance, 5)
        self.assertEqual(receiver.balance, 5)


class AccountBonusTest(TestCase):
    def setUp(self):
        self.obj = Account(number=12345, kind=Account.BONUS)
        self.obj.save()

    def test_deposit(self):
        self.obj.deposit(10)
        self.assertEqual(self.obj.balance, 10)

    def test_withdraw(self):
        self.obj.deposit(10)
        self.obj.withdraw(5)
        self.assertEqual(self.obj.balance, 5)

    def test_transfer(self):
        receiver = Account(number=67890)
        self.obj.deposit(10)
        self.obj.transfer(receiver, 5)
        self.assertEqual(self.obj.balance, 5)
        self.assertEqual(receiver.balance, 5)


class AccountSavingsTest(TestCase):
    def setUp(self):
        self.obj = Account(number=12345, kind=Account.SAVINGS)
        self.obj.save()

    def test_deposit(self):
        self.obj.deposit(10)
        self.assertEqual(self.obj.balance, 10)

    def test_withdraw(self):
        self.obj.deposit(10)
        self.obj.withdraw(5)
        self.assertEqual(self.obj.balance, 5)

    def test_transfer(self):
        receiver = Account(number=67890)
        self.obj.deposit(10)
        self.obj.transfer(receiver, 5)
        self.assertEqual(self.obj.balance, 5)
        self.assertEqual(receiver.balance, 5)

    def test_earn_interest(self):
        self.obj.deposit(10)
        self.obj.earn_interest(10)
        self.assertEqual(self.obj.balance, 11)
