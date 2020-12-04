class Bank:
    numberOfCustomers = 0

    def __init__(self, bankName, customers):
        self.bankName = bankName
        self.customers = customers

    def addCustomer(self, f, l):
        self.customers.append(Customer(f, l))
        self.numberOfCustomers += 1

    def getNumberOfCustomers(self):
        return self.numberOfCustomers

    def getCustomer(self, index):
        return self.customers[index]


class Customer():
    def __init__(self, f, l):
        self.firstName = f
        self.lastName = l
        self.account = Account()

    def __repr__(self):
        return "(% s ,% s)" % (self.firstName, self.lastName)

    def getFName(self):
        return self.firstName

    def getLName(self):
        return self.lastName

    def getAccount(self):
        return self.account

    def setAccount(self, acc):
        self.account = acc


class Account():
    # class variable
    noOfAccounts = 0

    def __init__(self, balance=1000):
        self.balance = balance  # instance variable

    def getBalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False

customers = []
bca = Bank("BCA", customers)

def choices():
    user_input = input("What would you like to do today? (a. balance, b. deposit, c. withdraw, or d. exit): ")
    if user_input == 'a':
        print('\nBalance:', bca.getCustomer(0).getAccount().getBalance())
        cont = input("\n Would you like to continue?: ")
        if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
            choices()
        elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
            print("Thank you for using BCA")
            main()

    elif user_input == 'b':
        deposit_amount = int(input("\nInput the amount you want to deposit: "))
        deposit_process = bca.getCustomer(0).getAccount().deposit(deposit_amount)
        if deposit_process is True:
            print("\nTransaction is successful!")
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                choices()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Thank you for using BCA")
                main()
        else:
            print('\nTransaction failed!')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                choices()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Thank you for using BCA")
                main()

    elif user_input == 'c':
        withdraw_amount = int(input("\nInput the amount you want to withdraw: "))
        withdraw_process = bca.getCustomer(0).getAccount().withdraw(withdraw_amount)
        if withdraw_process is True:
            print("\nTransaction is successful!")
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                choices()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Thank you for using BCA")
                main()
        else:
            print('\nTransaction failed!')
            cont = input("\n Would you like to continue?: ")
            if cont == "yes" or cont == "Yes" or cont == 'y' or cont == 'Y':
                choices()
            elif cont == "no" or cont == "No" or cont == 'n' or cont == 'N':
                print("Thank you for using BCA")
                main()

    elif user_input == 'd':
        print("Thank you for using BCA")
        main()

def main():
    def customer_exist():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        if first_name in customers and last_name in customers:
            print(bca.getCustomer(0).getAccount())
            # ask what would you like today
            choices()
        elif first_name not in customers and last_name not in customers:
            print("There is no account that is called", first_name, last_name)
            main()

    def new_account():
        print("Create a new account")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        bca.addCustomer(first_name, last_name)
        bca.getNumberOfCustomers()
        # ask what would you like today
        choices()

    # ask whether user have an account
    print("Welcome to BCA!")
    ask = input("Do you have an account?: ")
    if ask == "yes" or ask == "Yes" or ask == 'y' or ask == 'Y':
        customer_exist()
    elif ask == "no" or ask == "No" or ask == 'n' or ask == 'N':
        new_account()


if __name__=="__main__":
    main()
