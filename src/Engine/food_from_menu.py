from src.Engine.Basket import *
from src.DataSource import is_testing

def inport_menu():
    orderInput.menu = {}
    with open("resource\Entities\menu.txt", "r") as file:
        for data in file.readlines():
            data = data.lower()
            data = data.strip()
            data = data.split("^")
            orderInput.menu[data[0]] = data[1]
        return orderInput.menu

def orderInput(menu):

    orderInput.menu = menu
    orderInput.amountOfItem = {}

    orderInput.amountOfItem = orderInput.menu.copy()

    for value in orderInput.amountOfItem:
        orderInput.amountOfItem[value] = 0

    for value in orderInput.menu:
        orderInput.menu[value] = float(orderInput.menu[value])


    counter = 0
    print(orderInput.menu)
    total = []
    testing = is_testing.is_testing()
    while counter == 0:
        if testing == True:
            itemSelection = "tea"
            itemSelectionAmount = 4
            orderInput.amountOfItem[itemSelection] = orderInput.amountOfItem[itemSelection] + int(itemSelectionAmount)
            print(orderInput.amountOfItem)
            return[orderInput.amountOfItem]
        else:
            itemSelection = input("Please select an item off the order menu you would like to purchase")
            if itemSelection in orderInput.menu:
                itemSelectionAmount = input("Enter the amount of " + itemSelection + " would you like to add to your basket?: ")
                orderInput.amountOfItem[itemSelection] = orderInput.amountOfItem[itemSelection] + int(itemSelectionAmount)
                print("You now have x" + str(orderInput.amountOfItem[itemSelection]), itemSelection + " in your basket")
            else:
                print("Sorry we don't sell that here")
            decision = input("Would you like to add anything else to your order? Y/N:")
            if decision.upper() == "N":
                basket(orderInput.menu, orderInput.amountOfItem)


