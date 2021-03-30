from src.Engine.input import *
from src.Engine.view_receipt import CreateReceipt

def basket():
    choice = "0"

    while choice == "0":
        cost = 0
        print("=================")
        print("Current Basket")
        print("=================")
        for product in orderInput.amountOfItem:
            if orderInput.amountOfItem[product] > 0:
                itemCost = (orderInput.amountOfItem[product])*(orderInput.menu[product])
                print("x" + str(orderInput.amountOfItem[product]), product,"£" + str("{:.2f}".format(itemCost)))
                cost += float(orderInput.amountOfItem[product])*float(orderInput.menu[product])
        print("=================")
        print("Total Cost: £", "{:.2f}".format(cost))
        print("")
        print("")
        choice = input("Would you like to edit your basket?(Y/N): ")

        if choice.upper() == "Y":
            basketEdit()

        elif choice.upper() == "N":
            CreateReceipt(orderInput.menu,orderInput.amountOfItem )



def basketEdit():
    print("==========================")
    print("1. Add item(s) to your basket")
    print("2. Remove item(s) from your basket")
    print("3. Exit")
    print("==========================")

    option = int(input("Enter number to proceed: "))

    edit = "Y"

    if option == 1:
        while edit == "Y":
            itemSelection = orderInput("What item would you like to add to your basket?: ")
            itemSelectionAmount = orderInput("Enter the amount of " + itemSelection + " would you like to add to your basket?: ")
            orderInput.amountOfItem[itemSelection] = orderInput.amountOfItem[itemSelection] + int(itemSelectionAmount)
            print("You now have x" + str(orderInput.amountOfItem[itemSelection]), itemSelection + " in your basket")
            edit = orderInput("Would you like add anything else? Y/N: ")

        if edit == "N":
            basket()
    elif option == 2:
        while edit == "Y":
            itemSelection = orderInput("What item would you like to remove from your basket?: ")
            itemSelectionAmount = orderInput("Enter the amount of " + itemSelection + " would you like to remove from your basket?: ")
            orderInput.amountOfItem[itemSelection] = orderInput.amountOfItem[itemSelection] - int(itemSelectionAmount)
            if orderInput.amountOfItem[itemSelection] < 0:
                orderInput.amountOfItem[itemSelection] = 0
            print("You now have x" + str(orderInput.amountOfItem[itemSelection]), itemSelection + " in your basket")
            edit = orderInput("Would you like remove anything else? Y/N: ")

        if edit == "N":
            basket()

    elif option == 3:
        basket()


    else:
        print("Error: Not a valid choice")


basket()
