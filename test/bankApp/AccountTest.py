import unittest

from src.bankApp.Account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()


    def test_that_balance_is_at_its_initial_state_0(self):
        self.assertEqual(0, self.account.balance())



    def test_that_if_i_deposit_2000_balance_is_20000(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(2000, self.account.deposit(2000))



    def test_that_if_i_deposit_a_negative_amount_balance_doesnt_change(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(0, self.account.deposit(-100))
        self.assertEqual(3000, self.account.deposit(3000))
        self.assertEqual(3000, self.account.deposit(-1000))



    def test_that_deposit_is_only_above_or_equal_to_500(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(0, self.account.deposit(400))



    def test_that_balance_cannot_be_below_0(self):
        self.assertEqual(0, self.account.balance())



    def test_that_if_balance_is_6000_and_i_withdraw_4000_balance_is_2000(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(6000, self.account.deposit(6000))
        self.assertEqual(6000, self.account.balance())
        self.assertEqual(2000, self.account.withdraw(4000, "754"))



    def test_that_if_i_try_to_withdraw_an_amount_greater_than_my_balance_my_balance_still_remains_the_same(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(5000,self.account.deposit(5000))
        self.assertEqual(5000,self.account.withdraw(7000, "754"))



    def test_that_if_i_withdraw_a_negative_amount_my_balance_doesnt_change(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(5000, self.account.deposit(5000))
        self.assertEqual(5000, self.account.balance())
        self.assertEqual(5000,self.account.withdraw( -43000, "754"))


    #
    def test_that_if_my_balance_is_1500_and_i_transfer_500_balance_is_1000(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(1500,self.account.deposit(1500))
        self.assertEqual(1500, self.account.balance())
        self.assertEqual(1000,self.account.transfer(500, "754"))



    def test_that_amount_to_be_transferred_cant_be_greater_than_balance_and_if_so_balance_remains_the_same(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(600,self.account.deposit(600))
        self.assertEqual(600,self.account.balance())
        self.assertEqual(600,self.account.transfer(650, "754"))



    def test_that_amount_to_be_transferred_is_less_than_0_balance_doesnt_change(self):
        self.assertEqual(0, self.account.balance())
        self.assertEqual(1000,self.account.deposit(1000))
        self.assertEqual(1000,self.account.balance())
        self.assertEqual(1000,self.account.transfer(-4300,"754"))


