from src.DataSource.order_adapter import order_number_adapt
from src.DataSource.order_to_file import save_order_to_file
import sys

def create_receipt(menu, quantity):

    order_store = True
    save_order = []
    order_number = order_number_adapt()
    item_quantity = list(quantity.values())
    item_selected = list(quantity.keys())
    item_price = list(menu.values())
    order_total = 0
    item_index = 0

    print("Order Number: #" + order_number + "\n")
    save_order.append("Order Number:" + order_number)
    for quantity in item_quantity:
       if quantity == 0:
        item_index += 1
        continue
       print(str(item_quantity[item_index]) + " " + item_selected[item_index] + ": £" + str(item_price[item_index]) + "0")
       save_order.append(item_quantity[item_index])
       save_order.append(str(item_selected[item_index]))
       save_order.append("£"+str(item_price[item_index]))
       order_total += item_quantity[item_index] * item_price[item_index]
       item_index += 1
    print("\nTOTAL: £" + str(order_total) + "0")
    save_order.append(order_total)
    if order_number == "TEST00":
        return save_order
    else:
        save_order_to_file(order_store,save_order)
        sys.exit("Thank you for your order")

