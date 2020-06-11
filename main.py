from utilities.user import *
from utilities.application import *
import sys, os, json
# Initialize the application
def ask_for_input(display_string, acceptable_responses):
    """Asks for input from the user. If the input is
    accepted, we return the input. If not, we ask again.

    Parameters
    ----------
    display_string : string
        String to display and ask for a response.

    acceptable_responses : list
        List of responses we expect

    Returns
    -------
    user_input : string
        String for user input
    """
    user_input = input(display_string)
    if user_input not in acceptable_responses:
        user_input = ask_for_input(display_string, acceptable_responses)
    else:
        return user_input


if __name__ == "__main__":
    application = Application()
    user_input = ask_for_input("Welcome to Jenny's Python banking service. Is this your first time? (y, n) ", ['y', 'n'])
    if user_input == "y":
        print("""

        This is a pretty basic setup. Some supported operations include:
            1. Creating an account.
            2. Adding saving/checking accounts.
            3. Withdrawing/depositing money into your accounts.
            4. Calculating interest rates.

        """)

        user_input = ask_for_input("Would you like to create an account? (y, n) ", ['y', 'n'])

        if user_input == 'y':
            username = input("Please enter your account username: ")
            password = input("Please enter your account password: ")
            print("Alright, {}. We just made your account. Please log into your account with the username and password.".format(username))
            application.create_account(username, password)
            application.log_out_user()
            sys.exit()

        if user_input == 'n':
            print("Alright, have a nice day!")
            sys.exit()

    else:
        username = input("What is your username? ")
        password = input("What is your password? ")
        response = application.load(username, password)

        if response == False:
            print("Something's wrong with your username or password. Please try again. ")
        else:
            while True:
                acceptable_responses = ['withdraw', 'deposit', 'add account', 'list balances', 'exit', 'calculate interest']
                decision_string = "What would you like to do? {} "
                user_input = ask_for_input(decision_string.format(acceptable_responses), acceptable_responses)
                accounts = application.list_all_accounts()

                if user_input == 'exit':
                    application.save()
                    print("Thanks for using our services!")
                    sys.exit()

                if user_input == 'withdraw':
                    withdraw_string = "What account would you like to withdraw from? {} "
                    account = ask_for_input(withdraw_string.format(accounts), accounts)
                    amount = float(input("How much would you like to withdraw? "))
                    application.withdraw(account, amount)

                if user_input == 'deposit':
                    deposit_string = "What account would you like to deposit into? {} "
                    account = ask_for_input(deposit_string.format(accounts), accounts)
                    amount = input("How much would you like to deposit? ")
                    application.deposit(account, amount)

                if user_input == 'add acount':
                    account_name = input("What would you like this account to be named? ")
                    application.add_account(account_name)

                if user_input == 'list balances':
                    application.list_balances()

                if user_input == 'calculate interest':
                    try:
                        account = input("Which account would you like to calculate compound interest on?" )
                        rate = float(input("What's the interest rate on this account? (integer/float ) "))
                        n = int(input("What's the amount of times interest will be applied? (per time period, integer) " ))
                        t = float(input("How many time periods will you be going through? (integer/float) "))
                        result = application.calculate_interest(account, rate, n, t)
                        print("Your final balance will be: {}".format(result))
                    except:
                        print("Sorry, you must've entered a value incorrectly. Make sure you follow the specified format.")
                        break
