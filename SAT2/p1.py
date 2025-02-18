class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def get_name(self):
        return self.name


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customers(self):
        return [customer.get_name() for customer in self.customers]



account1 = Account(1000)
customer1 = Customer("avni", account1)

bank = Bank()
bank.add_customer(customer1)

print(f"Bank Customers: {bank.get_customers()}")
print(customer1.account.deposit(500))
print(customer1.account.withdraw(200))
print(f"avni's balance: {customer1.account.get_balance()}")
