from src.DataSource import is_testing
from src.Engine.view_receipt import create_receipt

def basket(orderMenu, itemAmount):
    choice = "0"

    while choice == "0":
        cost = 0
        print("=================")
        print("Current Basket")
        print("=================")
        for product in itemAmount:
            if itemAmount[product] > 0:
                itemCost = (itemAmount[product])*(orderMenu[product])
                print("x" + str(itemAmount[product]), product,"£" + str("{:.2f}".format(itemCost)))
                cost += float(itemAmount[product])*float(orderMenu[product])
        print("=================")
        print("Total Cost: £", "{:.2f}".format(cost))
        print("")
        print("")
        testing = is_testing.is_testing()
        if testing == True:
            choice = "N"
        else:
            choice = input("Would you like to edit your basket?(Y/N): ")

        if choice.upper() == "Y":
            basketEdit(orderMenu, itemAmount)

        elif choice.upper() == "N":
            testing = is_testing.is_testing()
            if testing == True:
                testingOutput = [orderMenu, itemAmount]
                return testingOutput
            else:
                create_receipt(orderMenu, itemAmount)


def basketEdit(orderMenu, itemAmount, testing):
    print("==========================")
    print("1. Add item(s) to your basket")
    print("2. Remove item(s) from your basket")
    print("3. Exit")
    print("==========================")

    option = int(input("Enter number to proceed: "))

    edit = "Y"

    if option == 1:
        while edit == "Y":
            itemSelection = input("What item would you like to add to your basket?: ")
            itemSelectionAmount = input("Enter the amount of " + itemSelection + " would you like to add to your basket?: ")
            itemAmount[itemSelection] = itemAmount[itemSelection] + int(itemSelectionAmount)
            print("You now have x" + str(itemAmount[itemSelection]), itemSelection + " in your basket")
            edit = input("Would you like add anything else? Y/N: ")

        if edit == "N":
            basket(orderMenu, itemAmount, testing)
    elif option == 2:
        while edit == "Y":
            itemSelection = input("What item would you like to remove from your basket?: ")
            itemSelectionAmount = input("Enter the amount of " + itemSelection + " would you like to remove from your basket?: ")
            itemAmount[itemSelection] = itemAmount[itemSelection] - int(itemSelectionAmount)
            if itemAmount[itemSelection] < 0:
                itemAmount[itemSelection] = 0
            print("You now have x" + str(itemAmount[itemSelection]), itemSelection + " in your basket")
            edit = input("Would you like remove anything else? Y/N: ")

        if edit == "N":
            basket(orderMenu, itemAmount)

    elif option == 3:
        basket(orderMenu, itemAmount)

    else:
        print("Error: Not a valid choice")


