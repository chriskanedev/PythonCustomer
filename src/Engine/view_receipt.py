from src.DataSource.order_adapter import order_number_adapt
from src.DataSource.order_to_file import save_order_to_file
import sys

def Create_Receipt(menu,quantity):

    order_store = True
    save_order = []
    order_number = order_number_adapt()
    item_quantity = list(quantity.values())
    item_selected = list(quantity.keys())
    item_price = list(menu.values())
    order_total = 0
    index = 0

    print("Order Number: #" + order_number + "\n")
    save_order.append("Order Number:" + order_number)
    for quantity in item_quantity:
       if quantity == 0:
        index += 1
        continue
       print(str(item_quantity[index]) + " " + item_selected[index] + ": £" + str(item_price[index]) + "0")
       save_order.append(item_quantity[index])
       save_order.append(str(item_selected[index]))
       save_order.append("£"+str(item_price[index]))
       order_total += item_quantity[index] * item_price[index]
       index += 1
    print("\nTOTAL: £" + str(order_total) + "0")
    save_order.append(order_total)
    if order_number == "TEST00":
        return save_order
    else:
        save_order_to_file(order_store,save_order)
        sys.exit("Thank you for your order")

