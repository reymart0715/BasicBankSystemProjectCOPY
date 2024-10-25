from Account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = Account(name, initial_balance)
            print(f"Account created for {name} with balance {initial_balance}")
        else:
            print("Account already exists for this name.")

    def get_account(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            print("Account not found.")
            return None


