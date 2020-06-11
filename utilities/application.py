from utilities.user import *
import sys, os, json

class Application:
    # Initialize application; make references to current working directory & data storage
    def __init__(self):
        self.current_path = os.path.abspath(os.path.dirname(__file__))
        self.data_path = self.current_path + "/data/"
        self.user = None

    def create_account(self, username, password):
        """Creates a user account and sets the current user to the new account.

        Parameters
        ----------
        username : string
            String for desired username.

        password : string
            String for desired password

        Returns
        -------
        None
            Creates the user account and saves the data to a .json file.
        """
        self.user = User(username, password)
        self.save()

    def validate(self, username, password):
        """ Validates the user credentials before performing operations.

        Parameters
        ----------
        username : string
            String for username.

        password : string
            String for password

        Returns
        -------
        data_dict : dict
            If successful, returns dictionary containing user information.

        boolean
            Otherwise, returns False if encounters an error.
        """
        target_data = self.data_path + "{}.json".format(username)
        try:
            target_file = open(target_data, 'r').read()
        except:
            print("Error when looking up your account, are you sure you have an account with us?")
            return False

        try:
            data_dict = json.loads(target_file)

        except:
            print("Error when retrieving data. Are you sure you have an account with us?")
            return False

        else:
            target_password = data_dict["password"]
            if password == target_password:
                print("Account successfully validated.")
                return data_dict

            elif password != target_password:
                print("Incorrect password.")
                return False


    def load(self, username, password):
        """Validates the username, password and loads the user information if
        successful.

        Parameters
        ----------
        username : string
            String for username.

        password : string
            String for password

        Returns
        -------
        None
            If successful, loads the user information into the application.
            Otherwise, prints an error and exits.
        """
        validation = self.validate(username, password)

        if not validation:
            # validate() will print out corresponding error.
            # print("Error while validating. Check credentials.")
            return False

        else:
            self.user = User(username, password)
            self.user.accounts = validation["accounts"]
            print("Successfully loaded: {}".format(username))
            return True

    def check_user_state(self):
        """Checks the current user state.

        Returns
        -------
        boolean
            Returns True if there currently is a valid user.
            Raises an error and returns False otherwise.
        """
        if self.user == None:
            print("Currently no user. Invalid operation.")
            return False
        else:
            return True

    def retrieve_user_data(self):
        """ Utility method for retrieving user_data.

        Parameters
        ----------

        Returns
        -------
        tuple
            Returns a tuple containing username, password, accounts if
            validation is successful.

        """
        if self.check_user_state() == True:
            return self.user.get_name(), self.user.get_password(), self.user.get_accounts()

    def print_user_data(self):
        """ Utility method for printing user_data.
        Prints the tuple containing username, password, accounts if
        validation is successful.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if self.check_user_state() == True:
            print(self.retrieve_user_data())

    def save(self):
        """ Saves the current user_data.

        Parameters
        ----------
        None

        Returns
        -------
        boolean
            Returns False if an error occurs - either during
            validation or checking the current user state.

            Otherwise, saves the current user data into a .json file
            in the data directory.
        """
        if self.check_user_state() == True:
            username, password, accounts = self.retrieve_user_data()
            user_path = self.data_path + "{}.json".format(username)
            load_data = {
                "username" : username,
                "password" : password,
                "accounts" : accounts
            }
            with open(user_path, 'w+') as json_file:
                json.dump(load_data, json_file)
        else:
            print("Error while retrieving user data.")
            return False

    # Accessing the user account
    def deposit(self, account, amount):
        self.user.add_balance(account, amount)

    def withdraw(self, account, amount):
        self.user.withdraw_balance(account, amount)

    def add_account(self, account):
        self.user.add_account(account)

    def show_balance(self, account):
        self.user.show_balance(account)

    def list_all_accounts(self):
        return list(self.user.get_accounts().keys())

    def list_balances(self):
        print(self.user.get_accounts())

    def log_out_user(self):
        self.user = None

    def calculate_interest(self, account, rate, n, t):
        return self.user.calculate_interest(account, rate, n, t)
