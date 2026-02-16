class Account:

    def __init__(self, pin):
        self.__balance = 0
        self.__PIN = pin

    def balance(self) -> int:
            return self.__balance

    def deposit(self, amount: int)-> int:
        if amount >= 500:
            self.__balance = self.__balance + amount

        return self.__balance

    def pin_is_valid(self,pin):
        return self.__PIN == pin


    def withdraw(self, amount: int, pin: str):
        if not self.pin_is_valid(pin):
            return "Invalid PIN"
        if  self.__balance > amount and amount >= 500:
            self.__balance -= amount


        return self.__balance



    def transfer(self, amount: int, pin: str):
        if not self.pin_is_valid(pin):
            return "Invalid PIN"
        if self.__balance > amount and amount >= 500:
            self.__balance -= amount

        return self.__balance


    def validate_amount(self, amount: int)-> bool:
        if amount < 0:
            return False
        return True

