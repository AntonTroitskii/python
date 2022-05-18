import random


class Account(object):
    # переменная, используемая всеми экземплярами класса
    num_account = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_account += 1

    def __del__(self):
        Account.num_account -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance


class EvilAccount(Account):
    def __init__(self, name, balance, evilfactor):
        Account.__init__(self, name, balance)  # Вызов метода инициализации
        # базового класса Account
        self.evilfactor = evilfactor

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * 1.10
        else:
            return self.balance


class MoreEvilAcount(EvilAccount):

    def deposit(self, amt):
        self.withdraw(5.00)  # Вычесть плату за “удобство”
        # EvilAccount.deposit(self, amt)  # А теперь пополнить счет
        super(MoreEvilAcount, self).deposit(amt)


class DepositCharge(object):
    fee = 5.00

    def deposit_fee(self):
        self.withdraw(self.fee)


class WithdrawCharge(object):
    fee = 2.50

    def withdraw_fee(self):
        self.withdraw(self.fee)


# Класс, использующий механизм множественного наследования
class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
    def deposit(self, amt):
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)

    def withdraw(self, amt):
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)


# Создание экземпляров класса
a = Account("Гвидо", 100.0)
b = Account("Билл", 1000.0)

c = EvilAccount("Джордж", 1000.0)
c.deposit(10.0)

avaliable = c.inquiry()
print(avaliable)
