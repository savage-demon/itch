# Банковский счёт
#
# Создайте класс BankAccount, описывающий банковский счёт.
#
# Объект должен хранить имя владельца и текущий баланс.
#
# Реализуйте методы:
#
# пополнение счёта
#
# снятие средств
#
# отображение баланса
#
# При попытке снять больше, чем есть на счёте, операция не должна выполняться.
#
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
#
#
# История операций
#
# Доработайте класс BankAccount.
#
# Каждая операция пополнения и снятия должна сохраняться в историю.
#
# История должна быть доступна через property history только для чтения.
#
# История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).
#


class BankAccount:
    """Банковский счёт с защищённым балансом и историей операций."""

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        """Возвращает копию истории, не позволяя изменить её извне."""
        return self.__history.copy()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            return False
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")
        return True

    def display_balance(self):
        print(f"Balance: {self.__balance}")


if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    account.deposit(150)
    account.withdraw(100)
    account.withdraw(500)

    account.display_balance()
    print(account.history)
