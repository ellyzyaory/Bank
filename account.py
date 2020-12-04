class account:
    def __init__(self, balance = 1000):
        self.balance = balance #instance variable

    def getbalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            return True
        else:
            return False
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            return True
        else:
            return False

def main():
    def user():
        user_input = input("What would you like to do today? (a. balance, b. deposit, c. withdraw, or d. exit): ")

        if user_input == 'a':
            print('\nBalance:', user_account.getbalance(), '\n')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                user()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Exit")


        elif user_input == 'b':
            deposit_amount = int(input("\nInput the amount you want to deposit: "))
            deposit_process = user_account.deposit(deposit_amount)
            if deposit_process is True:
                print("\nTransaction is successful!")
            else:
                print('\nTransaction failed!')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                user()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Exit")


        elif user_input == 'c':
            withdraw_amount = int(input("\nInput the amount you want to withdraw: "))
            withdraw_process = user_account.withdraw(withdraw_amount)
            if withdraw_process is True:
                print("\nTransaction is successful!")
            else:
                print('\nTransaction failed!')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                user()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Exit")

        elif user_input == 'd':
            print("Exit")


    def new_user():
        user_input = input("What would you like to do today? (a. balance, b. deposit, c. withdraw, or d. exit): ")

        if user_input == 'a':
            print('\nBalance:', new_account.getbalance())
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                new_user()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Exit")

        elif user_input == 'b':
            deposit_amount = int(input("\nInput the amount you want to deposit: "))
            deposit_process = new_account.deposit(deposit_amount)
            if deposit_process is True:
                print("\nTransaction is successful!")
            else:
                print('\nTransaction failed!')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                new_user()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Exit")


        elif user_input == 'c':
            withdraw_amount = int(input("\nInput the amount you want to withdraw: "))
            withdraw_process = new_account.withdraw(withdraw_amount)
            if withdraw_process is True:
                print("\nTransaction is successful!")
            else:
                print('\nTransaction failed!')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                new_user()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Exit")

        elif user_input == 'd':
            print("Exit")

    ask_account = input("Welcome! Do you have an account?: ")
    if ask_account == "yes" or ask_account == "Yes" or ask_account == 'y' or ask_account == 'Y':
        print("\nWelcome back!")
        user_account = account(10000)
        user()

    elif ask_account == "no" or ask_account == "No" or ask_account == 'n' or ask_account == 'N':
        ask_account2 = input("\nWould you like to make an account?: ")
        if ask_account2 == "yes" or ask_account2 == "Yes" or ask_account2 == 'y' or ask_account2 == 'Y':
            new_account = account(1000)
            new_user()

        elif ask_account2 == "no" or ask_account2 == "No" or ask_account2 == 'n' or ask_account2 == 'N':
            print("\nThere is no account \n Exit")


if __name__=="__main__":
    main()
