class Account:
    id = 0
    def __init__(self, account_holder , account_balance):
        Account.id += 1
        self.__account_holder  = account_holder 
        self.__account_balance  = account_balance 
        self.__account_number = Account.id

    def deposit(self, amount):
        self.__account_balance += amount
        print("New balance after deposit:", self.__account_balance)

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print("New balance after withdrawal:", self.__account_balance)
        else:
            print("Insufficient funds...")

    def check_balance(self):
        print(f"Current balance is {self.__account_balance}")

    def get_account_holder(self):
        print("Account holder:", self.__account_holder)

    def get_account_number(self):
        print("Account number:", self.__account_number)

# Testing
my_account = Account("Ali", 1000000)
my_account.get_account_number()
my_account.get_account_holder()
my_account.check_balance()
my_account.deposit(500000)
my_account.withdraw(200000)

# Testing
my_account = Account("Mohamed", 2000000)
my_account.get_account_number()
my_account.get_account_holder()
my_account.check_balance()
my_account.deposit(600000)
my_account.withdraw(300000)

# Testing
my_account = Account("Margo", 3000000)
my_account.get_account_number()
my_account.get_account_holder()
my_account.check_balance()
my_account.deposit(700000)
my_account.withdraw(400000)