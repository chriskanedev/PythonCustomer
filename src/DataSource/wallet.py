class TestCustomerWallet:
    def __init__(self):
        self.balance = 0
        print("Hello, you can now deposit money to your wallet")

    def deposit(self):
        while True:
            try:
                amount = float(input("How much would you like to add to your wallet?: "))
                self.balance += amount
                print("\n Amount Deposited:", amount)
                break
            except ValueError:
                print("\n This is not a number. Please try again.")
                print()

    def display(self):
        print("\n Available Balance=", self.balance)


wallet = TestCustomerWallet()

wallet.deposit()
wallet.display()
