import json, copy

class User:
    # Initializes user - sets username and password, also sets default accounts
    def __init__(self, username, password):
        self.credentials = {
            "username" : username,
            "password" : password
        }
        self.accounts = {
            "checkings" : 0.0,
            "savings" : 0.0
        }

    # Utility methods to just get information (self-explanatory)
    def get_name(self):
        return self.credentials["username"]

    def get_password(self):
        return self.credentials["password"]

    def get_accounts(self):
        return self.accounts

    def show_balance(self, account):
        """Shows the desired balance

        Parameters
        ----------
        account : string
            String for account name.

        Returns
        -------
        None
            If successful, prints the account balance.
            Otherwise, prints an error and exits.
        """
        account_balance = self.get_balance(account)
        if account_balance != None:
            print(account_balance)
        else:
            print("Error while retrieving balance.")
            return None

    def get_balance(self, account):
        """Gets the desired balance.
        If successful, returns the account balance.
        Otherwise, prints an error and exits.

        Parameters
        ----------
        account : string
            String for account name.

        Returns
        -------
        balance : int/float
            Number for the balance
        """
        if account not in self.accounts.keys():
            print("Account not in user profile.")
        else: return self.accounts[account]

    def add_balance(self, account_type, amount):
        """Adds amount to desired account
        If successful, adds the account balance.
        Otherwise, prints an error and exits.

        Parameters
        ----------
        account_type : string
            String for account name.

        amount : float
            Balance to add to the account

        Returns
        -------
        None

        """
        float_amount = float(amount)
        if float_amount < 0:
            print("Can't do anything with negative money.")
            return

        if account_type in self.accounts:
            self.accounts[account_type] += float_amount
        else:
            print("Account not in user profile.")
            return

    def withdraw_balance(self, account, amount):
        """Withdraws the desired balance after checking that the account
        exists and there are sufficient funds.
        If successful, withdraws the account balance.
        Otherwise, prints an error and exits.

        Parameters
        ----------
        account : string
            String for account name.

        amount : float
            Desired withdrawal amount

        Returns
        -------
        None
        """
        float_amount = float(amount)
        if float_amount < 0:
            print("Can't do anything with negative money!")
            return

        if account not in self.accounts:
            print("Account not in user profile.")
            return
        if self.accounts[account] < amount:
            print("Insufficient funds in {} account.".format(account))
            return
        self.accounts[account] -= float_amount

    def add_account(self, new_account):
        """Adds an account to the user profile.
        Simply adds the account to user and sets the balance to 0

        Parameters
        ----------
        new_account : string
            String for account name.

        Returns
        -------
        None
        """
        new_accounts = {}
        for account in self.accounts:
            new_accounts[account] = self.accounts[account]
        new_accounts[new_account] = 0.0
        self.accounts = new_accounts

    def calculate_interest(self, account, rate, n, t):
        """Calculates compound interest for a specified account.

        Parameters
        ----------
        account : string
            String for account name when we look up principal balance.

        rate : float/int
            Number for interest rate

        n : int
            Integer for amount of times interest will be calculated in a period

        t : int/float
            Number for amount of time (years)

        Returns
        -------
        None
        """
        principal_balance = self.accounts[account]
        result = principal_balance * (1 + (rate / n)) ** (n * t)
        return result
