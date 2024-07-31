import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = Account(initial_balance=100)
        self.account2 = Account(initial_balance=25)
    
    def test_withdraw_success(self):
        self.account1.withdraw(50)
        self.assertEqual(self.account1.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(150)
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(-10)

    def test_deposit_success(self):
       self.account1.deposit(50)
       self.assertEqual(self.account1.balance, 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(-20)

    def test_deposit_no_amount(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(0)

    def test_transfer_success(self):
        self.account1.transfer(self.account2, 50)
        self.assertEqual(self.account1.balance, 50)
        self.assertEqual(self.account2.balance, 75)

    def test_transfer_account_doesnt_exist(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(None, 50)

if __name__ == '__main__':
    unittest.main()
