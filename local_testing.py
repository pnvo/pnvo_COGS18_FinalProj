from utilities.user import *
from utilities.application import *

def create_test_user():
    return User(username = 'test', password = '12345')

test_user = create_test_user()

# Testing all of the user methods
def test_username():
    expected_username = 'test'
    actual_username = test_user.get_name()
    assert expected_username == actual_username

def test_password():
    expected_password = '12345'
    actual_password = test_user.get_password()
    assert expected_password == actual_password

def test_accounts():
    expected_accounts_count = 2
    actual_accounts_count = len(list(test_user.get_accounts()))
    assert expected_accounts_count == actual_accounts_count

def test_get_balance():
    expected_balance = 0
    actual_balance = test_user.get_balance('checkings')
    assert expected_balance == actual_balance
    test_user.show_balance('checkings')
    test_user.show_balance('savings')
    test_user.get_balance('nonexisting')

def test_add_account():
    new_account = 'savings-2'
    test_user.add_account(new_account)
    print(test_user.get_accounts())

def test_interest_rate():
    user = create_test_user()
    user.accounts['checkings'] = 1000
    rate = 3.5
    n = 10
    t = 10
    print(user.calculate_interest('checkings', rate, n, t))

# Integration test
def sequence_balance_updates():
    current_balance = test_user.get_balance('checkings')
    assert current_balance == 0
    test_user.add_balance('checkings', 10)
    assert test_user.get_balance('checkings') == 10
    test_user.withdraw_balance('checkings', 10) == 0
    test_user.withdraw_balance('nonexisting', 10)

def run_user_tests():
    test_username()
    test_password()
    test_accounts()
    test_get_balance()
    sequence_balance_updates()
    test_add_account()


# run_user_tests()
test_interest_rate()

# Application testing

application = Application()

# Unit tests
def test_application_create_account():
    application.create_account(username='test', password='12345')

def test_validate():
    application.create_account(username='test', password='12345')
    application.validate(username='test', password='12345')
    # application.validate(username='asd', password='asd')

def test_application_interest():
    application.create_account(username='test', password='12345')
    application.deposit('checkings', 1000)
    application.calculate_interest('checkings', 3.5, 10, 10)

def test_load():
    application.load('jenny', '12345')
    # application.load('nonexisting', '123')

def integration_test():
    # application.print_user_data()
    application.withdraw('checkings', 0)
    application.deposit('checkings', 100)
    # application.print_user_data()
    application.withdraw('checkings', 50)
    # application.print_user_data()
    application.add_account('new-account')
    application.deposit('new-account', 1000)
    # application.print_user_data()
    application.withdraw('new-account', .2)
    application.print_user_data()

def run_application_tests():
    test_application_create_account()
    # test_validate()
    # test_load() # Should encompass loading user data
    integration_test()

# run_application_tests()
test_application_interest()
